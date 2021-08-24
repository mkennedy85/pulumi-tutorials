

# Creating EC2 instance using tf2pulumi conversion tool. 

This lab could be done either by using the tf2pulumi tool or using the online tool

Link for tf2pulumi conversion tool https://www.pulumi.com/tf2pulumi/

## Install the tool
```
brew install pulumi/tap/tf2pulumi

```

## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```
    pulumi stack init ec2-tf-pul
    ```

2. Set the AWS region:

    ```
    pulumi config set aws:region us-east-1
    
    ```
4. Now convert the following terraform main.tf file into Pulumi file using tf2pulumi tool. ( remove the __main__.py file )

```
cd lab19-tf-to-pulumi
tf2pulumi --target-language python

```

5. Check the __main__.py file

```
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

```
6. The output of tf2pulumi conversion tool for ec2-instance is shown below & replace the content of __main__.py with below code. ( in case you used the webtool instead of command line tool )

```
import pulumi
import pulumi_aws as aws

my_ec2_vm = aws.ec2.Instance("my-ec2-vm",
                             ami="ami-04db49c0fb2215364",
                             availability_zone="ap-south-1a",
                             instance_type="t2.micro",
                             tags={
                                 "Name": "web",
                             })

```

7. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.
 ```   
 Previewing update (ec2-tf-pul)

     Type                 Name                     Plan
 +   pulumi:pulumi:Stack  tf-to-pulumi-ec2-tf-pul  create
 +   └─ aws:ec2:Instance  my-ec2-vm                create

Resources:
    + 2 to create
```
Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
```
> yes
  no
  details

```


8. Now, go to AWS console, navigate to EC2 service & check the ec2 instance with name "my-ec2-vm":
 

9. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
