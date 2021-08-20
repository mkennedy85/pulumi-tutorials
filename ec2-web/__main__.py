import pulumi
import pulumi_aws as aws

size = 't2.micro'
ami = aws.get_ami(most_recent="true",
                  owners=["137112412989"],
                  filters=[{"name": "name", "values": ["amzn-ami-hvm-*"]}])

group = aws.ec2.SecurityGroup('webserver-secgrp',
                              description='Enable HTTP access',
                              ingress=[
                                  {'protocol': 'tcp', 'from_port': 22,
                                      'to_port': 22, 'cidr_blocks': ['0.0.0.0/0']},
                                  {'protocol': 'tcp', 'from_port': 80,
                                      'to_port': 80, 'cidr_blocks': ['0.0.0.0/0']}
                                  # ^-- ADD THIS LINE
                              ])

user_data = """
#!/bin/bash
echo "<h1>Hello, Welcome to Pulumi Webinar!</h1>" > index.html
nohup python -m SimpleHTTPServer 80 &
"""
# ^-- ADD THIS DEFINITION

server = aws.ec2.Instance('webserver-www',
                          instance_type=size,
                          # reference security group from above
                          vpc_security_group_ids=[group.id],
                          user_data=user_data,  # <-- ADD THIS LINE
                          ami=ami.id)

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)
