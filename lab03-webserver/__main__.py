import pulumi
import pulumi_aws as aws

# Resources Block
# Resource-1: Create VPC
vpc_dev = aws.ec2.Vpc("vpc-dev",
                      cidr_block="10.0.0.0/16",
                      enable_dns_hostnames=True,
                      tags={
                          "Name": "vpc-dev",
                      })
# Resource-2: Create Subnets
vpc_dev_public_subnet_1 = aws.ec2.Subnet("vpc-dev-public-subnet-1",
                                         vpc_id=vpc_dev.id,
                                         cidr_block="10.0.1.0/24",
                                         availability_zone="us-west-2a",
                                         map_public_ip_on_launch=True)
# Resource-3: Internet Gateway
vpc_dev_igw = aws.ec2.InternetGateway("vpc-dev-igw", vpc_id=vpc_dev.id)
# Resource-4: Create Route Table
vpc_dev_public_route_table = aws.ec2.RouteTable(
    "vpc-dev-public-route-table", vpc_id=vpc_dev.id)
# Resource-5: Create Route in Route Table for Internet Access
vpc_dev_public_route = aws.ec2.Route("vpc-dev-public-route",
                                     route_table_id=vpc_dev_public_route_table.id,
                                     destination_cidr_block="0.0.0.0/0",
                                     gateway_id=vpc_dev_igw.id)
# Resource-6: Associate the Route Table with the Subnet
vpc_dev_public_route_table_associate = aws.ec2.RouteTableAssociation("vpc-dev-public-route-table-associate",
                                                                     route_table_id=vpc_dev_public_route_table.id,
                                                                     subnet_id=vpc_dev_public_subnet_1.id)
# Resource-7: Create Security Group
dev_vpc_sg = aws.ec2.SecurityGroup("mike-dev-vpc-sg",
                                   description="Dev VPC Default Security Group",
                                   vpc_id=vpc_dev.id,
                                   ingress=[
                                       {
                                           "description": "Allow Port 22",
                                           "from_port": 22,
                                           "to_port": 22,
                                           "protocol": "tcp",
                                           "cidr_blocks": ["0.0.0.0/0"],
                                       },
                                       {
                                           "description": "Allow Port 80",
                                           "from_port": 80,
                                           "to_port": 80,
                                           "protocol": "tcp",
                                           "cidr_blocks": ["0.0.0.0/0"],
                                       },
                                   ],
                                   egress=[{
                                       "description": "Allow all IP and Ports Outbound",
                                       "from_port": 0,
                                       "to_port": 0,
                                       "protocol": "-1",
                                       "cidr_blocks": ["0.0.0.0/0"],
                                   }])
# Resource-8: Create EC2 Instance
my_ec2_vm = aws.ec2.Instance("my-ec2-vm",
                             ami="ami-083ac7c7ecf9bb9b0",
                             instance_type="t2.micro",
                            #  key_name="demo-ec2",
                             subnet_id=vpc_dev_public_subnet_1.id,
                             vpc_security_group_ids=[dev_vpc_sg.id],
                             user_data="""#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl enable httpd
sudo systemctl start httpd
echo "<h1>Welcome to Pulumi Training! AWS Infra created using Pulumi in us-west-2 Region</h1>" > /var/www/html/index.html
""",
                             tags={
                                 "Name": "mike-ec2vm",
                             })

pulumi.export('publicIp', my_ec2_vm.public_ip)
pulumi.export('publicHostName', my_ec2_vm.public_dns)
