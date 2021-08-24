

# Create an EC2 instance & export the resource values. 

## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```
    pulumi stack init ec2-out

    ```

2. Set the AWS region:

    ```
    pulumi config set aws:region ap-south-1

    ```

3. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.

    ```  
     Type                      Name                     Plan +   pulumi:pulumi:Stack       ec2-output-demo-ec2-out  create
 +   ├─ aws:ec2:SecurityGroup  vpc-web                  create
 +   ├─ aws:ec2:SecurityGroup  vpc-ssh                  create
 +   └─ aws:ec2:Instance       my-ec2-vm                create

Resources:
    + 4 to create
Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
```
> yes
  no
  details

    ```

4. Now, go to AWS console, navigate to EC2 service & see the public_ip , private_ip etc of ec2 instance.The same values can be checked in the terminal window:
 ```
Outputs:
    ec2InstancePrivateip: "172.31.44.47"
    ec2InstancePublicip : "13.234.204.132"
    ec2Publicdns        : "http://ec2-13-234-204-132.ap-south-1.compute.amazonaws.com"
    ec2SecurityGroups   : [
        [0]: "vpc-ssh-19e913f"
        [1]: "vpc-web-e3f544b"
    ]
```



5. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
