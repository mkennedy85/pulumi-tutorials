"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
stack = pulumi.get_stack()
bucket = s3.Bucket("my-bucket-"+pulumi.get_stack())

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
