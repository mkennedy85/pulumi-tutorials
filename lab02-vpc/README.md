

# Create a custom VPC in AWS


## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```
    pulumi stack init website-testing
    ```

2. Set the AWS region:

    ```
    pulumi config set aws:region us-west-2
    ```

3. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.

    ```
    pulumi up
   Previewing update (vpc-stack)

     Type                 Name                Plan
 +   pulumi:pulumi:Stack  vpc-demo-vpc-stack  create
 +   └─ aws:ec2:Vpc       myvpc               create
 
Resources:
    + 2 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details
    ```

4. Now, go to AWS console, check the created vpc "myvpc":
 

5. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
