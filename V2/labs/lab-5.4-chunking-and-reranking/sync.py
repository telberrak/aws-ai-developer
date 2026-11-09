"""Upload the documents, then run an ingestion job on BOTH Knowledge Bases and wait for them.

Usage:  python sync.py docs
"""
import pathlib
import sys
import time

import boto3

from stack_outputs import KBS, kb, outputs


def upload(folder: pathlib.Path, bucket: str) -> None:
    s3 = boto3.client("s3")
    for path in sorted(folder.iterdir()):
        if path.is_file():
            s3.upload_file(str(path), bucket, path.name)
            print(f"  uploaded  {path.name}")


def ingest_all(out: dict) -> None:
    agent = boto3.client("bedrock-agent")
    jobs = {}
    for name in KBS:
        kb_id, ds_id = kb(out, name)
        jobs[name] = agent.start_ingestion_job(knowledgeBaseId=kb_id, dataSourceId=ds_id)["ingestionJob"]
    print("\nIngestion jobs started on both Knowledge Bases", end="", flush=True)

    # Both jobs run at the same time; poll until neither is still running.
    while any(j["status"] in ("STARTING", "IN_PROGRESS", "STOPPING") for j in jobs.values()):
        time.sleep(5)
        print(".", end="", flush=True)
        for name, job in jobs.items():
            kb_id, ds_id = kb(out, name)
            jobs[name] = agent.get_ingestion_job(knowledgeBaseId=kb_id, dataSourceId=ds_id,
                                                 ingestionJobId=job["ingestionJobId"])["ingestionJob"]
    print()
    for name, job in jobs.items():
        s = job.get("statistics", {})
        print(f"  {name:9} {job['status']:9} scanned {s.get('numberOfDocumentsScanned', 0)}, "
              f"indexed {s.get('numberOfNewDocumentsIndexed', 0) + s.get('numberOfModifiedDocumentsIndexed', 0)}, "
              f"failed {s.get('numberOfDocumentsFailed', 0)}")
        for reason in job.get("failureReasons", []):
            print("    reason:", reason)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not pathlib.Path(sys.argv[1]).is_dir():
        sys.exit("Usage: python sync.py <folder>")
    out = outputs()
    print(f"Uploading {sys.argv[1]} to s3://{out['SourceBucket']}")
    upload(pathlib.Path(sys.argv[1]), out["SourceBucket"])
    ingest_all(out)
