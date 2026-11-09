"""Lecture 6.4 demo: a versioned prompt in Prompt Management, used by a Bedrock Flow behind an alias.

Deploy:  cdk deploy                       (uses the model in cdk.json)
         cdk deploy -c model_id=<id>      (or pick another text model)
"""
import aws_cdk as cdk
from aws_cdk import aws_bedrock as bedrock
from aws_cdk import aws_iam as iam
from constructs import Construct

# Version 1 of the prompt. release.py writes version 2 later, outside CloudFormation.
PROMPT_V1 = (
    "You help a support team triage tickets.\n"
    "Read the ticket and return three lines:\n"
    "Summary: one sentence.\n"
    "Sentiment: positive, neutral or negative.\n"
    "Next action: what the agent should do first.\n\n"
    "Ticket: {{ticket}}"
)


class PromptFlowStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        model_id = self.node.try_get_context("model_id") or "amazon.nova-micro-v1:0"

        # 1. The prompt in Prompt Management: a template, one variable, a model and its settings.
        prompt = bedrock.CfnPrompt(
            self, "Prompt",
            name="lab-6-4-ticket-triage",
            description="Summarizes a support ticket for an agent.",
            default_variant="main",
            variants=[bedrock.CfnPrompt.PromptVariantProperty(
                name="main",
                template_type="TEXT",
                model_id=model_id,
                inference_configuration=bedrock.CfnPrompt.PromptInferenceConfigurationProperty(
                    text=bedrock.CfnPrompt.PromptModelInferenceConfigurationProperty(
                        temperature=0.2, max_tokens=300,
                    ),
                ),
                template_configuration=bedrock.CfnPrompt.PromptTemplateConfigurationProperty(
                    text=bedrock.CfnPrompt.TextPromptTemplateConfigurationProperty(
                        text=PROMPT_V1,
                        input_variables=[bedrock.CfnPrompt.PromptInputVariableProperty(name="ticket")],
                    ),
                ),
            )],
        )

        # 2. Version 1: an immutable snapshot of the prompt. The flow points at this, never at the draft.
        prompt_v1 = bedrock.CfnPromptVersion(
            self, "PromptV1", prompt_arn=prompt.attr_arn, description="First release",
        )

        # 3. The role the flow runs as: read the prompt, call the model, nothing else.
        role = iam.Role(self, "FlowRole", assumed_by=iam.ServicePrincipal(
            "bedrock.amazonaws.com",
            conditions={"StringEquals": {"aws:SourceAccount": self.account}},
        ))
        role.add_to_policy(iam.PolicyStatement(
            actions=["bedrock:GetPrompt"],
            resources=[prompt.attr_arn, f"{prompt.attr_arn}:*"],
        ))
        # An inference profile ID (us.amazon..., eu.amazon...) routes to the base model in several Regions.
        base_model = model_id.split(".", 1)[1] if model_id.split(".")[0] in ("us", "eu", "apac", "global") else model_id
        role.add_to_policy(iam.PolicyStatement(
            actions=["bedrock:InvokeModel"],
            resources=[
                f"arn:aws:bedrock:*::foundation-model/{base_model}",
                f"arn:aws:bedrock:{self.region}:{self.account}:inference-profile/{model_id}",
            ],
        ))

        # 4. The flow: input -> prompt node (prompt version 1) -> output.
        F = bedrock.CfnFlow
        flow = F(
            self, "Flow",
            name="lab-6-4-ticket-flow",
            execution_role_arn=role.role_arn,
            definition=F.FlowDefinitionProperty(
                nodes=[
                    F.FlowNodeProperty(
                        name="FlowInput", type="Input",
                        configuration=F.FlowNodeConfigurationProperty(input={}),
                        outputs=[F.FlowNodeOutputProperty(name="document", type="String")],
                    ),
                    F.FlowNodeProperty(
                        name="Triage", type="Prompt",
                        configuration=F.FlowNodeConfigurationProperty(
                            prompt=F.PromptFlowNodeConfigurationProperty(
                                source_configuration=F.PromptFlowNodeSourceConfigurationProperty(
                                    resource=F.PromptFlowNodeResourceConfigurationProperty(
                                        prompt_arn=prompt_v1.attr_arn,
                                    ),
                                ),
                            ),
                        ),
                        inputs=[F.FlowNodeInputProperty(name="ticket", type="String", expression="$.data")],
                        outputs=[F.FlowNodeOutputProperty(name="modelCompletion", type="String")],
                    ),
                    F.FlowNodeProperty(
                        name="FlowOutput", type="Output",
                        configuration=F.FlowNodeConfigurationProperty(output={}),
                        inputs=[F.FlowNodeInputProperty(name="document", type="String", expression="$.data")],
                    ),
                ],
                connections=[
                    F.FlowConnectionProperty(
                        name="InputToTriage", type="Data", source="FlowInput", target="Triage",
                        configuration=F.FlowConnectionConfigurationProperty(
                            data=F.FlowDataConnectionConfigurationProperty(
                                source_output="document", target_input="ticket"),
                        ),
                    ),
                    F.FlowConnectionProperty(
                        name="TriageToOutput", type="Data", source="Triage", target="FlowOutput",
                        configuration=F.FlowConnectionConfigurationProperty(
                            data=F.FlowDataConnectionConfigurationProperty(
                                source_output="modelCompletion", target_input="document"),
                        ),
                    ),
                ],
            ),
        )
        flow.node.add_dependency(role)

        # 5. Flow version 1 and the alias "live" that apps call. Releasing = moving the alias.
        flow_v1 = bedrock.CfnFlowVersion(self, "FlowV1", flow_arn=flow.attr_arn, description="First release")
        alias = bedrock.CfnFlowAlias(
            self, "LiveAlias",
            flow_arn=flow.attr_arn,
            name="live",
            routing_configuration=[bedrock.CfnFlowAlias.FlowAliasRoutingConfigurationListItemProperty(
                flow_version=flow_v1.attr_version,
            )],
        )

        cdk.CfnOutput(self, "PromptId", value=prompt.attr_id)
        cdk.CfnOutput(self, "FlowId", value=flow.attr_id)
        cdk.CfnOutput(self, "FlowAliasId", value=alias.attr_id)


app = cdk.App()
PromptFlowStack(app, "PromptFlowDemo")
app.synth()
