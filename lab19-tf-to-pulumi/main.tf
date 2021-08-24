# Create EC2 Instance
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance

resource "aws_instance" "my-ec2-vm" {
    ami = "ami-04db49c0fb2215364"
    instance_type = "t2.micro"
    availability_zone = "ap-south-1a"
    #availability_zone = "us-east-1b"
    tags = {
        "Name" = "web"
        #"tag1" = "Update-test-1"
    }
}