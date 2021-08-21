import pulumi
import pulumi_aws as aws

config = pulumi.Config()
aws_region = config.get("awsRegion")
if aws_region is None:
    aws_region = "ap-south-1"
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
                                    "description": "Allow all ip and ports outboun",
                                    "from_port": 0,
                                    "to_port": 0,
                                    "protocol": "-1",
                                    "cidr_blocks": ["0.0.0.0/0"],
                                }])
# Create Security Group - Web Traffic
vpc_web = aws.ec2.SecurityGroup("vpc-web",
                                description="Dev VPC web",
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
                                    "description": "Allow all ip and ports outbound",
                                    "from_port": 0,
                                    "to_port": 0,
                                    "protocol": "-1",
                                    "cidr_blocks": ["0.0.0.0/0"],
                                }])
amzlinux = aws.get_ami(most_recent=True,
                       owners=["amazon"],
                       filters=[
                           {
                               "name": "name",
                               "values": ["amzn2-ami-hvm-*-gp2"],
                           },
                           {
                               "name": "root-device-type",
                               "values": ["ebs"],
                           },
                           {
                               "name": "virtualization-type",
                               "values": ["hvm"],
                           },
                           {
                               "name": "architecture",
                               "values": ["x86_64"],
                           },
                       ])
# Create EC2 Instance - Amazon Linux
my_ec2_vm = aws.ec2.Instance("my-ec2-vm",
                             ami=amzlinux.id,
                             instance_type=ec2_instance_type,                           
                             user_data=(lambda path: open(path).read())(
                                 "apache-install.sh"),
                             vpc_security_group_ids=[
                                 vpc_ssh.id,
                                 vpc_web.id,
                             ],
                             tags={
                                 "Name": "amz-linux-vm",
                             })
# Define Output Values
pulumi.export("ec2InstancePublicip", my_ec2_vm.public_ip)
pulumi.export("ec2Publicdns", my_ec2_vm.public_dns)
