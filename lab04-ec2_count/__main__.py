import pulumi
import pulumi_aws as aws

# Create EC2 Instance
web = []
for range in [{"value": i} for i in range(0, 2)]:
    web.append(aws.ec2.Instance(f"web-{range['value']}",
                                ami="ami-02f84cf47c23f1769",
                                instance_type="t2.micro",
                                tags={
                                    "Name": f"web-{range['value']}",
                                }))

config = pulumi.Config()
pulumi.export('web-0-publicIP', web[0].public_ip)
pulumi.export('web-1-publicIP', web[1].public_ip)
pulumi.export("DB password",config.get("dbpass"))

