

# Creating EC2 instance on AWS & configure it as apache web-server


## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```
    pulumi stack init ec2-webserver
    ```

2. Set the AWS region:

    ```
    pulumi config set aws:region ap-south-1
    ```

3. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.

    ```
    pulumi up
   Previewing update (ec2-webserver)      

     Type                              Name                                  Plan
 +   pulumi:pulumi:Stack               testing-ec2-ec2-webserver             create
 +   ├─ aws:ec2:Vpc                    vpc-dev                               create
 +   ├─ aws:ec2:Subnet                 vpc-dev-public-subnet-1               create
 +   ├─ aws:ec2:InternetGateway        vpc-dev-igw                           create
 +   ├─ aws:ec2:RouteTable             vpc-dev-public-route-table            create
 +   ├─ aws:ec2:SecurityGroup          dev-vpc-sg                            create
 +   ├─ aws:ec2:RouteTableAssociation  vpc-dev-public-route-table-associate  create
 +   ├─ aws:ec2:Route                  vpc-dev-public-route                  create
 +   └─ aws:ec2:Instance               my-ec2-vm                             create
 
Resources:
    + 9 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
 ```
> yes
  no
  details
    ```

4. Now, go to AWS console, navigate to EC2 service & check the created ec2 instance "my_ec2_vm":
 
5. Open the site URL in a browser with publicIp of ec2 instance & see the output.

5. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
