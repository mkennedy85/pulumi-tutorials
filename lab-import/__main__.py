import pulumi
import pulumi_aws as aws
from pulumi import ResourceOptions

# pulumi_imported_example = aws.s3.Bucket("pulumi-imported-example",
#     acl="private",
#     bucket="pulumi-import-example",
#     force_destroy=False,
#     opts=pulumi.ResourceOptions(protect=False))

# # IMPORTANT: Python appends an underscore (`import_`) to avoid conflicting with the keyword.

# group = aws.ec2.SecurityGroup('pulumi-imported-sg',
#     name='pulumi-import-sg',
#     description='pulumi-import-sg',
#     ingress=[
#         { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] },
#          { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] }
#     ],
#     opts=ResourceOptions(import_='sg-0456bf6c89d0ddde0'))

import pulumi_aws as aws
import pulumi_terraform as terraform

# Reference the Terraform state file:
network_state = terraform.state.RemoteStateReference('network',
    backend_type='local',
    args=terraform.state.LocalBackendArgs(path='/Users/chandank/work/terraform-aws-vpc-1/examples/simple-vpc/terraform.tfstate'))

# Read the VPC and subnet IDs into variables:
vpc_id = network_state.get_output('vpc_id')
public_subnet_ids = network_state.get_output('public_subnet_ids')

# Now spin up servers in the first two subnets:
for i in range(2):
    aws.ec2.Instance(f'instance-{i}',
        ami='ami-02b4e72b17337d6c1',
        instance_type='t2.micro',
        subnet_id=public_subnet_ids[i])