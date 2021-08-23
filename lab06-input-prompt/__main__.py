import pulumi
import pulumi_aws as aws

config = pulumi.Config("aws")
aws_region = config.get("region")
print("Region",aws_region)
if aws_region is "ca-central-1":
    ec2_ami_id = "ami-02f84cf47c23f1769"
ec2_instance_count = config.get_float("ec2InstanceCount")
if ec2_instance_count is None:
    ec2_instance_count = 1
ec2_instance_type = config.require("ec2InstanceType")
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
my_ec2_vm = []
for range in [{"value": i} for i in range(0, ec2_instance_count)]:
    my_ec2_vm.append(aws.ec2.Instance(f"my-ec2-vm-{range['value']}",
                                      ami=ec2_ami_id,
                                      instance_type=ec2_instance_type,
                                      user_data="""#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl enable httpd
sudo systemctl start httpd
echo "<h1>Welcome to Pulumi Training ! AWS Infra created using Pulumi in ap-south-1 Region</h1>" > /var/www/html/index.html
""",
                                      vpc_security_group_ids=[
                                          vpc_ssh.id,
                                          vpc_web.id,
                                      ],
                                      tags={
                                          "Name": "myec2vm",
                                      }))

pulumi.export('publicIp', my_ec2_vm[0].public_ip)
