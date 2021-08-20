"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

bucket = s3.Bucket('my-bucket',
                   website=s3.BucketWebsiteArgs(
                       index_document="index.html",
                   ))

bucketObject = s3.BucketObject(
    'index.html',
    acl='public-read',
    content_type='text/html',
    bucket=bucket,
    source=pulumi.FileAsset('index.html'),
)

pulumi.export('bucket_endpoint', pulumi.Output.concat(
    'http://', bucket.website_endpoint))

