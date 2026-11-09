"""Lecture 5.4 demo: one S3 source, two Knowledge Bases that differ only in chunking.

  fixed     small fixed-size chunks (100 tokens, almost no overlap)
  semantic  semantic chunks (up to 300 tokens, split where the meaning changes)

Both embed with Titan Text Embeddings V2 and store vectors in Amazon S3 Vectors.
Deploy:  cdk deploy
"""
import aws_cdk as cdk
from aws_cdk import aws_bedrock as bedrock
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3vectors as s3vectors
from constructs import Construct

EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"
DIMENSIONS = 1024

CHUNKING = {
    "fixed": bedrock.CfnDataSource.ChunkingConfigurationProperty(
        chunking_strategy="FIXED_SIZE",
        fixed_size_chunking_configuration=bedrock.CfnDataSource.FixedSizeChunkingConfigurationProperty(
            max_tokens=100, overlap_percentage=1,
        ),
    ),
    "semantic": bedrock.CfnDataSource.ChunkingConfigurationProperty(
        chunking_strategy="SEMANTIC",
        semantic_chunking_configuration=bedrock.CfnDataSource.SemanticChunkingConfigurationProperty(
            max_tokens=300, buffer_size=1, breakpoint_percentile_threshold=90,
        ),
    ),
}


class ChunkingStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # One source bucket, shared by both Knowledge Bases.
        source = s3.Bucket(
            self, "Source",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            enforce_ssl=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        # One vector bucket. Each Knowledge Base gets its own index in it.
        vector_bucket = s3vectors.CfnVectorBucket(self, "VectorBucket")

        embed_arn = f"arn:aws:bedrock:{self.region}::foundation-model/{EMBEDDING_MODEL_ID}"
        role = iam.Role(self, "KbRole", assumed_by=iam.ServicePrincipal(
            "bedrock.amazonaws.com",
            conditions={"StringEquals": {"aws:SourceAccount": self.account}},
        ))
        role.add_to_policy(iam.PolicyStatement(actions=["bedrock:InvokeModel"], resources=[embed_arn]))
        source.grant_read(role)

        for name, chunking in CHUNKING.items():
            index = s3vectors.CfnIndex(
                self, f"Index-{name}",
                vector_bucket_arn=vector_bucket.attr_vector_bucket_arn,
                index_name=f"kb-{name}",
                data_type="float32",
                dimension=DIMENSIONS,
                distance_metric="cosine",
                metadata_configuration=s3vectors.CfnIndex.MetadataConfigurationProperty(
                    non_filterable_metadata_keys=["AMAZON_BEDROCK_TEXT", "AMAZON_BEDROCK_METADATA"],
                ),
            )
            role.add_to_policy(iam.PolicyStatement(
                actions=["s3vectors:PutVectors", "s3vectors:GetVectors", "s3vectors:DeleteVectors",
                         "s3vectors:QueryVectors", "s3vectors:GetIndex"],
                resources=[index.attr_index_arn],
            ))

            kb = bedrock.CfnKnowledgeBase(
                self, f"Kb-{name}",
                name=f"lab-5-4-{name}",
                role_arn=role.role_arn,
                knowledge_base_configuration=bedrock.CfnKnowledgeBase.KnowledgeBaseConfigurationProperty(
                    type="VECTOR",
                    vector_knowledge_base_configuration=bedrock.CfnKnowledgeBase.VectorKnowledgeBaseConfigurationProperty(
                        embedding_model_arn=embed_arn,
                    ),
                ),
                storage_configuration=bedrock.CfnKnowledgeBase.StorageConfigurationProperty(
                    type="S3_VECTORS",
                    s3_vectors_configuration=bedrock.CfnKnowledgeBase.S3VectorsConfigurationProperty(
                        index_arn=index.attr_index_arn,
                    ),
                ),
            )
            kb.node.add_dependency(role)

            # The only difference between the two: the chunking configuration.
            # Chunking is fixed when the data source is created; to change it, create a new one.
            ds = bedrock.CfnDataSource(
                self, f"Ds-{name}",
                name=f"s3-docs-{name}",
                knowledge_base_id=kb.attr_knowledge_base_id,
                data_deletion_policy="DELETE",
                data_source_configuration=bedrock.CfnDataSource.DataSourceConfigurationProperty(
                    type="S3",
                    s3_configuration=bedrock.CfnDataSource.S3DataSourceConfigurationProperty(
                        bucket_arn=source.bucket_arn,
                    ),
                ),
                vector_ingestion_configuration=bedrock.CfnDataSource.VectorIngestionConfigurationProperty(
                    chunking_configuration=chunking,
                ),
            )

            label = name.capitalize()
            cdk.CfnOutput(self, f"{label}KnowledgeBaseId", value=kb.attr_knowledge_base_id)
            cdk.CfnOutput(self, f"{label}DataSourceId", value=ds.attr_data_source_id)

        cdk.CfnOutput(self, "SourceBucket", value=source.bucket_name)


app = cdk.App()
ChunkingStack(app, "ChunkingDemo")
app.synth()
