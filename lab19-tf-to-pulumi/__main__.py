
import pulumi
import pulumi_aws as aws

my_ec2_vm = aws.ec2.Instance("my-ec2-vm",
                             ami="ami-04db49c0fb2215364",
                             availability_zone="ap-south-1a",
                             instance_type="t2.micro",
                             tags={
                                 "Name": "web",
                             })
