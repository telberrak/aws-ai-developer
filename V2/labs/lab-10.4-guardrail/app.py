"""Lecture 10.4 demo: a Bedrock Guardrail that blocks prompt injection and masks PII.

Deploy:  cdk deploy
Then:    python test_guardrail.py      (ApplyGuardrail on test inputs, no model call)
         python chat.py "<message>"     (Converse with the guardrail attached)
"""
import aws_cdk as cdk
from aws_cdk import aws_bedrock as bedrock
from constructs import Construct

G = bedrock.CfnGuardrail


class GuardrailStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        guardrail = G(
            self, "Guardrail",
            name="lab-10-4-support-guardrail",
            description="Support assistant: blocks prompt attacks, investment advice and card numbers; masks contact details.",
            blocked_input_messaging="Sorry, I can't help with that request.",
            blocked_outputs_messaging="Sorry, I can't share that answer.",

            # 1. Content filters. PROMPT_ATTACK checks input only, so its output strength must be NONE.
            content_policy_config=G.ContentPolicyConfigProperty(filters_config=[
                G.ContentFilterConfigProperty(type="PROMPT_ATTACK", input_strength="HIGH", output_strength="NONE"),
                G.ContentFilterConfigProperty(type="HATE", input_strength="HIGH", output_strength="HIGH"),
                G.ContentFilterConfigProperty(type="INSULTS", input_strength="MEDIUM", output_strength="MEDIUM"),
                G.ContentFilterConfigProperty(type="SEXUAL", input_strength="HIGH", output_strength="HIGH"),
                G.ContentFilterConfigProperty(type="VIOLENCE", input_strength="MEDIUM", output_strength="MEDIUM"),
                G.ContentFilterConfigProperty(type="MISCONDUCT", input_strength="MEDIUM", output_strength="MEDIUM"),
            ]),

            # 2. A denied topic: a support bot must not give investment advice.
            topic_policy_config=G.TopicPolicyConfigProperty(topics_config=[
                G.TopicConfigProperty(
                    name="InvestmentAdvice",
                    type="DENY",
                    definition="Recommendations or guidance about buying, selling or holding stocks, funds, crypto or other investments.",
                    examples=[
                        "Should I buy shares in this company?",
                        "Which crypto will go up next month?",
                        "Is now a good time to move my pension into tech funds?",
                    ],
                ),
            ]),

            # 3. Sensitive information: mask contact details, block card numbers, plus one custom pattern.
            sensitive_information_policy_config=G.SensitiveInformationPolicyConfigProperty(
                pii_entities_config=[
                    G.PiiEntityConfigProperty(type="EMAIL", action="ANONYMIZE"),
                    G.PiiEntityConfigProperty(type="PHONE", action="ANONYMIZE"),
                    G.PiiEntityConfigProperty(type="NAME", action="ANONYMIZE"),
                    G.PiiEntityConfigProperty(type="CREDIT_DEBIT_CARD_NUMBER", action="BLOCK"),
                ],
                regexes_config=[
                    G.RegexConfigProperty(
                        name="OrderNumber",
                        description="Internal order IDs such as ORD-123456",
                        pattern=r"ORD-\d{6}",
                        action="ANONYMIZE",
                    ),
                ],
            ),
        )

        # 4. Version 1: an immutable snapshot. Apps call this number, not the working draft.
        version = bedrock.CfnGuardrailVersion(
            self, "GuardrailV1",
            guardrail_identifier=guardrail.attr_guardrail_id,
            description="First release",
        )

        cdk.CfnOutput(self, "GuardrailId", value=guardrail.attr_guardrail_id)
        cdk.CfnOutput(self, "GuardrailVersion", value=version.attr_version)


app = cdk.App()
GuardrailStack(app, "GuardrailDemo")
app.synth()
