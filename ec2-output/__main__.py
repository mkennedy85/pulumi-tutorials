import pulumi
import pulumi_aws as aws

config = pulumi.Config()
aws_region = config.get("awsRegion")
if aws_region is None:
    aws_region = "ap-south-1"
ec2_ami_id = config.get("ec2AmiId")
if ec2_ami_id is None:
    ec2_ami_id = "ami-04db49c0fb2215364"
ec2_instance_type = config.get("ec2InstanceType")
if ec2_instance_type is None:
    ec2_instance_type = "t2.micro"
# Create Security Group - SSH Traffic
vpc_ssh = aws.ec2.SecurityGroup("vpc-ssh",
                                description="Dev VPC SSH",
                                ingress=[{
                                    "description": "Allow Port 22",
                                    "from_port": 22,
                                    "to_port": 22,
                                    "protocol": "tcp",
                                    "cidr_blocks": ["0.0.0.0/0"],
                                }],
                                egress=[{
                                    "description": "Allow all IP and Ports outbound",
                                    "from_port": 0,
                                    "to_port": 0,
                                    "protocol": "-1",
                                    "cidr_blocks": ["0.0.0.0/0"],
                                }])
# Create Security Group - Web Traffic
vpc_web = aws.ec2.SecurityGroup("vpc-web",
                                description="Dev VPC Web",
                                ingress=[
                                    {
                                        "description": "Allow Port 80",
                                        "from_port": 80,
                                        "to_port": 80,
                                        "protocol": "tcp",
                                        "cidr_blocks": ["0.0.0.0/0"],
                                    },
                                    {
                                        "description": "Allow Port 443",
                                        "from_port": 443,
                                        "to_port": 443,
                                        "protocol": "tcp",
                                        "cidr_blocks": ["0.0.0.0/0"],
                                    },
                                ],
                                egress=[{
                                    "description": "Allow all IP and Ports outbound",
                                    "from_port": 0,
                                    "to_port": 0,
                                    "protocol": "-1",
                                    "cidr_blocks": ["0.0.0.0/0"],
                                }])
# Create EC2 Instance
my_ec2_vm = aws.ec2.Instance("my-ec2-vm",
                             ami=ec2_ami_id,
                             instance_type=ec2_instance_type,                             
                             user_data=(lambda path: open(path).read())(
                                 "apache-install.sh"),
                             vpc_security_group_ids=[
                                 vpc_ssh.id,
                                 vpc_web.id,
                             ],
                             tags={
                                 "Name": "web",
                             })
pulumi.export("ec2InstancePublicip", my_ec2_vm.public_ip)
pulumi.export("ec2InstancePrivateip", my_ec2_vm.private_ip)
pulumi.export("ec2SecurityGroups", my_ec2_vm.security_groups)
pulumi.export("ec2Publicdns", my_ec2_vm.public_dns.apply(
    lambda public_dns: f"http://{public_dns}"))
