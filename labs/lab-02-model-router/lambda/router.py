"""Model router: reads the model route from AppConfig, then calls Bedrock Converse."""
import json
import os
import time

import boto3

appconfig = boto3.client("appconfigdata")
bedrock = boto3.client("bedrock-runtime")

CACHE_SECONDS = int(os.environ.get("CACHE_SECONDS", "15"))
_state = {"token": None, "config": None, "fetched": 0.0}


def get_config() -> dict:
    """Return the routing config, polling AppConfig at most every CACHE_SECONDS."""
    now = time.time()
    if _state["config"] is not None and now - _state["fetched"] < CACHE_SECONDS:
        return _state["config"]
    if _state["token"] is None:
        _state["token"] = appconfig.start_configuration_session(
            ApplicationIdentifier=os.environ["APP_ID"],
            EnvironmentIdentifier=os.environ["ENV_ID"],
            ConfigurationProfileIdentifier=os.environ["PROFILE_ID"],
            RequiredMinimumPollIntervalInSeconds=15,
        )["InitialConfigurationToken"]
    resp = appconfig.get_latest_configuration(ConfigurationToken=_state["token"])
    _state["token"] = resp["NextPollConfigurationToken"]
    body = resp["Configuration"].read()
    if body:  # empty means "no change since the last poll"
        _state["config"] = json.loads(body)
    _state["fetched"] = now
    return _state["config"]


def handler(event, context):
    req = json.loads(event.get("body") or "{}")
    prompt = req.get("prompt", "What is Amazon Bedrock?")
    use_case = req.get("useCase", "default")

    cfg = get_config()
    route = cfg.get(use_case, cfg["default"])

    resp = bedrock.converse(
        modelId=route["modelId"],
        messages=[{"role": "user", "content": [{"text": prompt}]}],
        inferenceConfig={"temperature": route.get("temperature", 0.2), "maxTokens": route["maxTokens"]},
    )
    result = {
        "useCase": use_case,
        "modelId": route["modelId"],
        "answer": resp["output"]["message"]["content"][0]["text"],
        "usage": resp["usage"],
    }
    return {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": json.dumps(result)}
