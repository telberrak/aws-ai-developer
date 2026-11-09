"""Lecture 4.5 demo: a Bedrock Knowledge Base with an S3 source, stored in Amazon S3 Vectors.

Deploy:  cdk deploy
"""
import aws_cdk as cdk
from aws_cdk import aws_bedrock as bedrock
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3vectors as s3vectors
from constructs import Construct

# Titan Text Embeddings V2 returns 1024-dimension vectors by default.
EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"
DIMENSIONS = 1024


class KnowledgeBaseStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. The source: a plain S3 bucket that holds the documents.
        source = s3.Bucket(
            self, "Source",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            enforce_ssl=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        # 2. The vector store: an S3 vector bucket with one index.
        vector_bucket = s3vectors.CfnVectorBucket(self, "VectorBucket")
        index = s3vectors.CfnIndex(
            self, "Index",
            vector_bucket_arn=vector_bucket.attr_vector_bucket_arn,
            index_name="kb-index",
            data_type="float32",
            dimension=DIMENSIONS,
            distance_metric="cosine",
            # The chunk text and Bedrock's own metadata are too large for filterable metadata.
            metadata_configuration=s3vectors.CfnIndex.MetadataConfigurationProperty(
                non_filterable_metadata_keys=["AMAZON_BEDROCK_TEXT", "AMAZON_BEDROCK_METADATA"],
            ),
        )

        # 3. The role the Knowledge Base uses to read, embed and write.
        embed_arn = f"arn:aws:bedrock:{self.region}::foundation-model/{EMBEDDING_MODEL_ID}"
        role = iam.Role(self, "KbRole", assumed_by=iam.ServicePrincipal(
            "bedrock.amazonaws.com",
            conditions={"StringEquals": {"aws:SourceAccount": self.account}},
        ))
        role.add_to_policy(iam.PolicyStatement(actions=["bedrock:InvokeModel"], resources=[embed_arn]))
        source.grant_read(role)
        role.add_to_policy(iam.PolicyStatement(
            actions=["s3vectors:PutVectors", "s3vectors:GetVectors", "s3vectors:DeleteVectors",
                     "s3vectors:QueryVectors", "s3vectors:GetIndex"],
            resources=[index.attr_index_arn],
        ))

        # 4. The Knowledge Base itself.
        kb = bedrock.CfnKnowledgeBase(
            self, "KnowledgeBase",
            name="lab-4-5-kb",
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
        # The role's policy must exist before Bedrock validates access to the index.
        kb.node.add_dependency(role)

        # 5. The data source: the S3 bucket, split into fixed-size chunks.
        ds = bedrock.CfnDataSource(
            self, "DataSource",
            name="s3-docs",
            knowledge_base_id=kb.attr_knowledge_base_id,
            data_deletion_policy="DELETE",
            data_source_configuration=bedrock.CfnDataSource.DataSourceConfigurationProperty(
                type="S3",
                s3_configuration=bedrock.CfnDataSource.S3DataSourceConfigurationProperty(
                    bucket_arn=source.bucket_arn,
                ),
            ),
            vector_ingestion_configuration=bedrock.CfnDataSource.VectorIngestionConfigurationProperty(
                chunking_configuration=bedrock.CfnDataSource.ChunkingConfigurationProperty(
                    chunking_strategy="FIXED_SIZE",
                    fixed_size_chunking_configuration=bedrock.CfnDataSource.FixedSizeChunkingConfigurationProperty(
                        max_tokens=300, overlap_percentage=20,
                    ),
                ),
            ),
        )

        cdk.CfnOutput(self, "SourceBucket", value=source.bucket_name)
        cdk.CfnOutput(self, "KnowledgeBaseId", value=kb.attr_knowledge_base_id)
        cdk.CfnOutput(self, "DataSourceId", value=ds.attr_data_source_id)


app = cdk.App()
KnowledgeBaseStack(app, "KnowledgeBaseDemo")
app.synth()
