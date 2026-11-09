"""Circuit state in DynamoDB: count failures, open the circuit at a threshold, close it on success."""
import os
from datetime import datetime, timedelta, timezone

import boto3

table = boto3.resource("dynamodb").Table(os.environ["TABLE"])
THRESHOLD = int(os.environ["THRESHOLD"])
COOLDOWN = int(os.environ["COOLDOWN_SECONDS"])
KEY = {"pk": "primary"}


def record_failure(event, context):
    item = table.update_item(
        Key=KEY,
        UpdateExpression="ADD failures :one",
        ExpressionAttributeValues={":one": 1},
        ReturnValues="ALL_NEW",
    )["Attributes"]
    failures = int(item["failures"])
    if failures >= THRESHOLD:
        open_until = (datetime.now(timezone.utc) + timedelta(seconds=COOLDOWN)).strftime("%Y-%m-%dT%H:%M:%SZ")
        table.update_item(Key=KEY, UpdateExpression="SET openUntil = :t",
                          ExpressionAttributeValues={":t": open_until})
        return {"failures": failures, "state": "OPEN", "openUntil": open_until}
    return {"failures": failures, "state": "CLOSED"}


def reset(event, context):
    table.update_item(Key=KEY, UpdateExpression="SET failures = :zero REMOVE openUntil",
                      ExpressionAttributeValues={":zero": 0})
    return {"state": "CLOSED"}
