import pulumi
import pulumi_aws as aws
from pulumi import ResourceOptions

pulumi_imported_example = aws.s3.Bucket("pulumi-imported-example",
    acl="private",
    bucket="pulumi-import-example",
    force_destroy=False,
    opts=pulumi.ResourceOptions(protect=False))

# IMPORTANT: Python appends an underscore (`import_`) to avoid conflicting with the keyword.

group = aws.ec2.SecurityGroup('pulumi-imported-sg',
    name='pulumi-import-sg',
    description='pulumi-import-sg',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] },
         { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] }
    ],
    opts=ResourceOptions(import_='sg-0456bf6c89d0ddde0'))