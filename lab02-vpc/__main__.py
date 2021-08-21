import pulumi
import pulumi_aws as aws

# Resource Block
# Resource-1: Create VPC
myvpc = aws.ec2.Vpc("myvpc",
                    cidr_block="10.0.0.0/16",
                    tags={
                        "Name": "myvpc",
                    })
