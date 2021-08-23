import pulumi
import pulumi_aws as aws

# Create EC2 Instance
web = []
for range in [{"value": i} for i in range(0, 2)]:
    web.append(aws.ec2.Instance(f"web-{range['value']}",
                                ami="ami-04db49c0fb2215364",
                                instance_type="t2.micro",
                                tags={
                                    "Name": f"web-{range['value']}",
                                }))

pulumi.export('web-0-publicIP', web[0].public_ip)
pulumi.export('web-1-publicIP', web[1].public_ip)

