import pulumi
import pulumi_aws as aws

config = pulumi.Config()
aws_region = config.get("awsRegion")
if aws_region is None:
    aws_region = "ap-south-1"
app_name = config.require("appName")
environment_name = config.require("environmentName")
bucket_name = f"{app_name}-{environment_name}-bucket"
# Create S3 Bucket - with Input Variables & Local Values
mys3bucket = aws.s3.Bucket("mys3bucket",
                           acl="private",
                           tags={
                               "Name": bucket_name,
                               "Environment": environment_name,
                           })
