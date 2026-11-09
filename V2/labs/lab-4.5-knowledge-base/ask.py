"""Ask the Knowledge Base a question.

Usage:  python ask.py "How long do I have to return an item?" --model <model-id-or-inference-profile-arn>
        python ask.py "How long do I have to return an item?" --retrieve-only
"""
import argparse

import boto3

from stack_outputs import outputs


def model_arn(model: str, region: str) -> str:
    if model.startswith("arn:"):
        return model
    # A cross-Region inference profile ID (for example us.<model>) is passed as its ID.
    if model.split(".")[0] in ("us", "eu", "apac", "global"):
        return model
    return f"arn:aws:bedrock:{region}::foundation-model/{model}"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("question")
    p.add_argument("--model", help="model ID, inference profile ID or ARN used to write the answer")
    p.add_argument("--retrieve-only", action="store_true", help="show the retrieved chunks, no generation")
    p.add_argument("--top", type=int, default=3)
    a = p.parse_args()

    kb_id = outputs()["KnowledgeBaseId"]
    rt = boto3.client("bedrock-agent-runtime")
    search = {"vectorSearchConfiguration": {"numberOfResults": a.top}}

    if a.retrieve_only:
        res = rt.retrieve(knowledgeBaseId=kb_id, retrievalQuery={"text": a.question},
                          retrievalConfiguration=search)
        for r in res["retrievalResults"]:
            uri = r["location"]["s3Location"]["uri"]
            print(f"\n[{r.get('score', 0):.3f}] {uri}\n{r['content']['text'][:300]}")
        return

    if not a.model:
        p.error("--model is required unless you use --retrieve-only")
    res = rt.retrieve_and_generate(
        input={"text": a.question},
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": kb_id,
                "modelArn": model_arn(a.model, rt.meta.region_name),
                "retrievalConfiguration": search,
            },
        },
    )
    print("\n" + res["output"]["text"] + "\n\nSources:")
    for cite in res.get("citations", []):
        for ref in cite["retrievedReferences"]:
            print("  -", ref["location"]["s3Location"]["uri"])


if __name__ == "__main__":
    main()
