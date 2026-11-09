"""Make the source bucket match a local folder, then run an ingestion job and print what changed.

Usage:  python sync.py docs/v1
"""
import hashlib
import pathlib
import sys
import time

import boto3

from stack_outputs import outputs


def mirror(folder: pathlib.Path, bucket: str) -> None:
    s3 = boto3.client("s3")
    remote = {o["Key"]: o["ETag"].strip('"')
              for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket)
              for o in page.get("Contents", [])}
    local = {p.name: p for p in sorted(folder.iterdir()) if p.is_file()}
    for key, path in local.items():
        if remote.get(key) == hashlib.md5(path.read_bytes()).hexdigest():
            print(f"  same      {key}")
            continue
        s3.upload_file(str(path), bucket, key)
        print(f"  {'updated' if key in remote else 'uploaded':9} {key}")
    for key in remote.keys() - local.keys():
        s3.delete_object(Bucket=bucket, Key=key)
        print(f"  deleted   {key}")


def ingest(kb_id: str, ds_id: str) -> None:
    agent = boto3.client("bedrock-agent")
    job = agent.start_ingestion_job(knowledgeBaseId=kb_id, dataSourceId=ds_id)["ingestionJob"]
    print(f"\nIngestion job {job['ingestionJobId']} started", end="", flush=True)
    while job["status"] in ("STARTING", "IN_PROGRESS", "STOPPING"):
        time.sleep(5)
        print(".", end="", flush=True)
        job = agent.get_ingestion_job(knowledgeBaseId=kb_id, dataSourceId=ds_id,
                                      ingestionJobId=job["ingestionJobId"])["ingestionJob"]
    print(f" {job['status']}")
    for reason in job.get("failureReasons", []):
        print("  reason:", reason)

    s = job.get("statistics", {})
    scanned = s.get("numberOfDocumentsScanned", 0)
    new = s.get("numberOfNewDocumentsIndexed", 0)
    modified = s.get("numberOfModifiedDocumentsIndexed", 0)
    failed = s.get("numberOfDocumentsFailed", 0)
    print(f"\n  scanned    {scanned}")
    print(f"  new        {new}")
    print(f"  modified   {modified}")
    print(f"  deleted    {s.get('numberOfDocumentsDeleted', 0)}")
    print(f"  unchanged  {max(scanned - new - modified - failed, 0)}")
    print(f"  failed     {failed}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not pathlib.Path(sys.argv[1]).is_dir():
        sys.exit("Usage: python sync.py <folder>")
    out = outputs()
    print(f"Syncing {sys.argv[1]} to s3://{out['SourceBucket']}")
    mirror(pathlib.Path(sys.argv[1]), out["SourceBucket"])
    ingest(out["KnowledgeBaseId"], out["DataSourceId"])
