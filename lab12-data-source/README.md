

# Get the latest Amazon Linux 2 AMI ID and reference that value when creating EC2 Instance resource ami = data.aws_ami.amzlinux.id. 

## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```
    pulumi stack init ec2-data

    ```

2. Set the AWS region:

    ```
    pulumi config set aws:region ap-south-1

    ```

3. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.

    ```  
Previewing update (ec2-data)

     Type                      Name                      Plan       Info
 +   pulumi:pulumi:Stack       ec2-data-source-ec2-data  create     1 warning
 +   ├─ aws:ec2:SecurityGroup  vpc-ssh                   create                                                        
 +   ├─ aws:ec2:SecurityGroup  vpc-web                   create
 +   └─ aws:ec2:Instance       my-ec2-vm                 create                                                        
 
Diagnostics:
  pulumi:pulumi:Stack (ec2-data-source-ec2-data):
    warning: get_ami is deprecated: aws.getAmi has been deprecated in favor of aws.ec2.getAmi


Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
```
> yes
  no
  details

```
4. Now, go to AWS console, navigate to EC2 service & see the public_ip , public_dns, ami_id etc of ec2 instance.The same values can be cross checked in the terminal window:

Outputs:
```
   Outputs:
    ami_id             : "ami-04db49c0fb2215364"
    ec2InstancePublicip: "13.232.199.81"
    ec2Publicdns       : "ec2-13-232-199-81.ap-south-1.compute.amazonaws.com"
```

5. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
