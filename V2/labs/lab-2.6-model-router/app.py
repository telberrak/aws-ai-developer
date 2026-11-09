"""Lecture 2.6 demo: a model router whose target model lives in AWS AppConfig.

Deploy:  cdk deploy -c modelId=<model-id-or-inference-profile-id>
"""
import json

import aws_cdk as cdk
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_appconfig as appconfig
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as lambda_
from constructs import Construct

CONFIG_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "required": ["default"],
    "additionalProperties": {
        "type": "object",
        "required": ["modelId", "maxTokens"],
        "properties": {
            "modelId": {"type": "string", "minLength": 3},
            "temperature": {"type": "number", "minimum": 0, "maximum": 1},
            "maxTokens": {"type": "integer", "minimum": 1, "maximum": 4096},
        },
    },
}


class ModelRouterStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, model_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        app = appconfig.CfnApplication(self, "App", name="model-router-demo")
        env = appconfig.CfnEnvironment(self, "Env", application_id=app.ref, name="lab")
        profile = appconfig.CfnConfigurationProfile(
            self, "Profile",
            application_id=app.ref,
            name="model-routing",
            location_uri="hosted",
            type="AWS.Freeform",
            validators=[appconfig.CfnConfigurationProfile.ValidatorsProperty(
                type="JSON_SCHEMA", content=json.dumps(CONFIG_SCHEMA))],
        )
        initial = {
            "default": {"modelId": model_id, "temperature": 0.2, "maxTokens": 400},
            "summarize": {"modelId": model_id, "temperature": 0.0, "maxTokens": 200},
        }
        version = appconfig.CfnHostedConfigurationVersion(
            self, "InitialVersion",
            application_id=app.ref,
            configuration_profile_id=profile.ref,
            content_type="application/json",
            content=json.dumps(initial),
        )
        appconfig.CfnDeployment(
            self, "InitialDeployment",
            application_id=app.ref,
            environment_id=env.ref,
            configuration_profile_id=profile.ref,
            configuration_version=version.ref,
            deployment_strategy_id="AppConfig.AllAtOnce",
        )

        fn = lambda_.Function(
            self, "Router",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="router.handler",
            code=lambda_.Code.from_asset("lambda"),
            timeout=cdk.Duration.seconds(60),
            environment={
                "APP_ID": app.ref,
                "ENV_ID": env.ref,
                "PROFILE_ID": profile.ref,
                "CACHE_SECONDS": "15",
            },
        )
        fn.add_to_role_policy(iam.PolicyStatement(
            actions=["appconfig:StartConfigurationSession", "appconfig:GetLatestConfiguration"],
            resources=[f"arn:aws:appconfig:{self.region}:{self.account}:application/{app.ref}/*"],
        ))
        # Lab simplification: any foundation model or inference profile. In production, list the exact ARNs.
        fn.add_to_role_policy(iam.PolicyStatement(
            actions=["bedrock:InvokeModel"],
            resources=[
                "arn:aws:bedrock:*::foundation-model/*",
                f"arn:aws:bedrock:*:{self.account}:inference-profile/*",
            ],
        ))

        api = apigw.RestApi(self, "Api", rest_api_name="model-router-demo",
                            deploy_options=apigw.StageOptions(throttling_rate_limit=5, throttling_burst_limit=10))
        api.root.add_resource("chat").add_method("POST", apigw.LambdaIntegration(fn))

        cdk.CfnOutput(self, "ChatUrl", value=api.url_for_path("/chat"))
        cdk.CfnOutput(self, "AppId", value=app.ref)
        cdk.CfnOutput(self, "EnvId", value=env.ref)
        cdk.CfnOutput(self, "ProfileId", value=profile.ref)


app = cdk.App()
ModelRouterStack(app, "ModelRouterDemo", model_id=app.node.try_get_context("modelId"))
app.synth()
