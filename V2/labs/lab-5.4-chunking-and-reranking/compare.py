"""Ask the same question in two ways and print the results side by side.

  python compare.py "question"                  fixed chunks vs semantic chunks, top 3 each
  python compare.py "question" --rerank         one Knowledge Base, vector order vs reranked order
  python compare.py "question" --rerank --kb semantic
                                                 choose the Knowledge Base (default: fixed)

Options:
  --top N         results to show (default 3)
  --candidates N  results the vector search returns before reranking (default 10)
  --reranker ID   reranker model ID (default amazon.rerank-v1:0; cohere.rerank-v3-5:0 also works)
"""
import argparse
import textwrap

import boto3

from stack_outputs import KBS, kb, outputs

WIDTH = 60


def retrieve(kb_id: str, question: str, n: int, rerank_arn: str = None, top: int = 3) -> list:
    search = {"numberOfResults": n}
    if rerank_arn:
        # Vector search returns n candidates; the reranker reads each one with the
        # question and keeps the best `top`.
        search["rerankingConfiguration"] = {
            "type": "BEDROCK_RERANKING_MODEL",
            "bedrockRerankingConfiguration": {
                "modelConfiguration": {"modelArn": rerank_arn},
                "numberOfRerankedResults": top,
            },
        }
    resp = boto3.client("bedrock-agent-runtime").retrieve(
        knowledgeBaseId=kb_id,
        retrievalQuery={"text": question},
        retrievalConfiguration={"vectorSearchConfiguration": search},
    )
    return resp["retrievalResults"]


def cell(result: dict) -> list:
    uri = result.get("location", {}).get("s3Location", {}).get("uri", "?")
    text = " ".join(result["content"]["text"].split())
    head = f"{result.get('score', 0):.3f}  {uri.rsplit('/', 1)[-1]}  ({len(text.split())} words)"
    return [head] + textwrap.wrap(text, WIDTH)[:4]


def side_by_side(left_title: str, left: list, right_title: str, right: list, top: int) -> None:
    print(f"\n{left_title:<{WIDTH}}   {right_title}")
    print(f"{'-' * WIDTH}   {'-' * WIDTH}")
    for i in range(top):
        a = cell(left[i]) if i < len(left) else []
        b = cell(right[i]) if i < len(right) else []
        for j in range(max(len(a), len(b))):
            x = a[j] if j < len(a) else ""
            y = b[j] if j < len(b) else ""
            prefix = f"{i + 1}. " if j == 0 else "   "
            print(f"{prefix}{x:<{WIDTH - 3}}   {prefix if y else ''}{y}")
        print()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("question")
    p.add_argument("--rerank", action="store_true")
    p.add_argument("--kb", choices=KBS, default="fixed")
    p.add_argument("--top", type=int, default=3)
    p.add_argument("--candidates", type=int, default=10)
    p.add_argument("--reranker", default="amazon.rerank-v1:0")
    a = p.parse_args()

    out = outputs()
    print(f"Q: {a.question}")
    if not a.rerank:
        results = {name: retrieve(kb(out, name)[0], a.question, a.top) for name in KBS}
        side_by_side("FIXED-SIZE CHUNKS (100 tokens)", results["fixed"],
                     "SEMANTIC CHUNKS (up to 300 tokens)", results["semantic"], a.top)
    else:
        region = boto3.session.Session().region_name
        arn = f"arn:aws:bedrock:{region}::foundation-model/{a.reranker}"
        kb_id = kb(out, a.kb)[0]
        before = retrieve(kb_id, a.question, a.candidates)
        after = retrieve(kb_id, a.question, a.candidates, rerank_arn=arn, top=a.top)
        side_by_side(f"VECTOR SEARCH ONLY ({a.kb})", before,
                     f"TOP {a.candidates}, RERANKED BY {a.reranker}", after, a.top)
        print("Scores on the left are similarity scores; on the right, relevance scores from the reranker.")
