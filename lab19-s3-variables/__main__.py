"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
stack = pulumi.get_stack()
config = pulumi.Config("aws")
aws_config = config.get("region")
project_config = pulumi.Config()
bucket_name = project_config.get("bucket_name")
print("Region",aws_config)


bucket = s3.Bucket(bucket_name +pulumi.get_stack())

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
