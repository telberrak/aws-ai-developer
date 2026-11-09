"""Lab 3: a Step Functions circuit breaker that fails over to a cross-Region inference profile.

Deploy:  cdk deploy -c primaryModelId=<model-id> -c fallbackModelId=<inference-profile-id>
"""
import aws_cdk as cdk
from aws_cdk import aws_dynamodb as ddb
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_stepfunctions_tasks as tasks
from constructs import Construct


class CircuitBreakerStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, primary: str, fallback: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = ddb.Table(
            self, "Circuit",
            partition_key=ddb.Attribute(name="pk", type=ddb.AttributeType.STRING),
            billing_mode=ddb.BillingMode.PAY_PER_REQUEST,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

        def fn(name: str, handler: str, timeout: int = 10) -> lambda_.Function:
            return lambda_.Function(
                self, name,
                runtime=lambda_.Runtime.PYTHON_3_12,
                handler=handler,
                code=lambda_.Code.from_asset("lambda"),
                timeout=cdk.Duration.seconds(timeout),
                environment={"TABLE": table.table_name, "THRESHOLD": "3", "COOLDOWN_SECONDS": "60"},
            )

        invoke_fn = fn("InvokeModel", "invoke.handler", 60)
        record_fn = fn("RecordFailure", "circuit.record_failure")
        reset_fn = fn("ResetCircuit", "circuit.reset")
        table.grant_read_write_data(record_fn)
        table.grant_read_write_data(reset_fn)
        # Lab simplification: any foundation model or inference profile. In production, list the exact ARNs.
        invoke_fn.add_to_role_policy(iam.PolicyStatement(
            actions=["bedrock:InvokeModel"],
            resources=["arn:aws:bedrock:*::foundation-model/*", f"arn:aws:bedrock:*:{self.account}:inference-profile/*"],
        ))

        get_circuit = tasks.DynamoGetItem(
            self, "Get circuit state",
            table=table,
            key={"pk": tasks.DynamoAttributeValue.from_string("primary")},
            consistent_read=True,
            result_path="$.circuit",
        )

        def call(name: str, model_id: str, role: str) -> tasks.LambdaInvoke:
            return tasks.LambdaInvoke(
                self, name,
                lambda_function=invoke_fn,
                payload=sfn.TaskInput.from_object({
                    "role": role,
                    "modelId": model_id,
                    "prompt": sfn.JsonPath.string_at("$.prompt"),
                    "simulateFailure.$": "$.simulateFailure",
                }),
                payload_response_only=True,
                result_path="$.result",
            )

        call_primary = call("Call primary model", primary, "primary")
        call_fallback = call("Call fallback (cross-Region profile)", fallback, "fallback")
        call_primary.add_retry(errors=["ThrottlingException"], max_attempts=2, backoff_rate=2,
                               interval=cdk.Duration.seconds(1))

        record = tasks.LambdaInvoke(self, "Record failure", lambda_function=record_fn,
                                    payload_response_only=True, result_path="$.breaker")
        reset = tasks.LambdaInvoke(self, "Close circuit", lambda_function=reset_fn,
                                   payload_response_only=True, result_path=sfn.JsonPath.DISCARD)
        done = sfn.Succeed(self, "Done")

        call_primary.add_catch(record, errors=["States.ALL"], result_path="$.error")
        record.next(call_fallback)
        call_fallback.next(done)
        call_primary.next(reset)
        reset.next(done)

        circuit_open = sfn.Condition.and_(
            sfn.Condition.is_present("$.circuit.Item.openUntil.S"),
            sfn.Condition.timestamp_greater_than_json_path("$.circuit.Item.openUntil.S", "$$.Execution.StartTime"),
        )
        definition = get_circuit.next(
            sfn.Choice(self, "Circuit open?")
            .when(circuit_open, call_fallback)
            .otherwise(call_primary)
        )

        machine = sfn.StateMachine(
            self, "Machine",
            state_machine_name="lab03-circuit-breaker",
            definition_body=sfn.DefinitionBody.from_chainable(definition),
            timeout=cdk.Duration.minutes(5),
        )
        cdk.CfnOutput(self, "StateMachineArn", value=machine.state_machine_arn)
        cdk.CfnOutput(self, "TableName", value=table.table_name)


app = cdk.App()
CircuitBreakerStack(app, "Lab03CircuitBreaker",
                    primary=app.node.try_get_context("primaryModelId") or "[in-region-model-id]",
                    fallback=app.node.try_get_context("fallbackModelId") or "[cross-region-inference-profile-id]")
app.synth()
