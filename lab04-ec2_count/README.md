

# Creating multiple EC2 instance on AWS. 

## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```
    pulumi stack init ec2-count
    ```

2. Set the AWS region:

    ```
    pulumi config set aws:region ca-central-1
    ```

3. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.

    ```
    Previewing update (ec2-count)

     Type                 Name                 Plan +   pulumi:pulumi:Stack  ec2-count-ec2-count  create
 +   ├─ aws:ec2:Instance  web-1                create
 +   └─ aws:ec2:Instance  web-0                create

Resources:    + 3 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
```
> yes
  no
  details
    ```

4. Now, go to AWS console, navigate to EC2 service & check the two ec2 instances with names "web-1" & "web-0":
 

5. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
