

# Creating EC2 web server using tf2pulumi conversion tool. 

Link for tf2pulumi conversion tool https://www.pulumi.com/tf2pulumi/

## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```
    pulumi stack init ec2-tf-pul-web
    ```

2. Set the AWS region:

    ```
    pulumi config set aws:region us-east-1
    
    ```
4. Now convert the following terraform main.tf file into Pulumi file using tf2pulumi tool.
```
# Input Variables
variable "aws_region" {
  description = "Region in which AWS Resources to be created"
  type = string
  default = "us-east-1"
}

variable "ec2_ami_id" {
  description = "AMI ID"
  type = string  
  default = "ami-0c2b8ca1dad447f8a"
}

variable "ec2_instance_count" {
  description = "EC2 Instance Count"
  type = number
  default = 1
}

variable "ec2_instance_type" {
  description = "EC2 Instance Type"
  type = string
  default = "t2.micro"
}

# Create Security Group - SSH Traffic
resource "aws_security_group" "vpc-ssh" {
  name        = "vpc-ssh"
  description = "Dev VPC SSH"
  ingress {
    description = "Allow Port 22"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    description = "Allow all IP and Ports outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create Security Group - Web Traffic
resource "aws_security_group" "vpc-web" {
  name        = "vpc-web"
  description = "Dev VPC Web"

  ingress {
    description = "Allow Port 80"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow Port 443"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all IP and Ports outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create EC2 Instance
resource "aws_instance" "my-ec2-vm" {
  ami           = var.ec2_ami_id 
  instance_type = var.ec2_instance_type
  count = var.ec2_instance_count
  user_data = file("apache-install.sh")  
  vpc_security_group_ids = [aws_security_group.vpc-ssh.id, aws_security_group.vpc-web.id]
  tags = {
    "Name" = "web"
  }
}

```
5. The output of tf2pulumi conversion tool for ec2-instance is shown below & replace the content of __main__.py with below code.

```
import pulumi
import pulumi_aws as aws

config = pulumi.Config()
aws_region = config.get("awsRegion")
if aws_region is None:
    aws_region = "us-east-1"
ec2_ami_id = config.get("ec2AmiId")
if ec2_ami_id is None:
    ec2_ami_id = "ami-0c2b8ca1dad447f8a"
ec2_instance_count = config.get_float("ec2InstanceCount")
if ec2_instance_count is None:
    ec2_instance_count = 1
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
my_ec2_vm = []
for range in [{"value": i} for i in range(0, ec2_instance_count)]:
    my_ec2_vm.append(aws.ec2.Instance(f"my-ec2-vm-{range['value']}",
        ami=ec2_ami_id,
        instance_type=ec2_instance_type,
        user_data=(lambda path: open(path).read())("apache-install.sh"),
        vpc_security_group_ids=[
            vpc_ssh.id,
            vpc_web.id,
        ],
        tags={
            "Name": "web",
        }))

```

6. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.
 ```   
 Previewing update (ec2-tf-pul-web)

     Type                      Name                             Plan
 +   pulumi:pulumi:Stack       lab20-tf2pul-web-ec2-tf-pul-web  create
 +   ├─ aws:ec2:SecurityGroup  vpc-ssh                          create
 +   ├─ aws:ec2:SecurityGroup  vpc-web                          create
 +   └─ aws:ec2:Instance       my-ec2-vm-0                      create
 
Resources:    + 4 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details

```

7. Now, go to AWS console, navigate to EC2 service & check the ec2 instance with name "my-ec2-vm-0":
 
8. Open the site URL in a browser with publicIp of ec2 instance & see the output.

9. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
