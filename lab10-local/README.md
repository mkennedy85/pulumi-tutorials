

# Create S3 Bucket with tags name- with Input Variables & Local Values. 

## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```
    pulumi stack init s3-input-local

    ```

2. Set the AWS region:

    ```
    pulumi config set aws:region ap-south-1
    pulumi config set s3-local-values:appName demo
    pulumi config set s3-local-values:environmentName prod

    ```

3. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.

    ```  
     Type                 Name                            Plan +   pulumi:pulumi:Stack  s3-local-values-s3-input-local  create
 +   └─ aws:s3:Bucket     mys3bucket                      create

Resources:
    + 2 to create
Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
```
> yes
  no
  details

    ```

4. Now, go to AWS console, navigate to S3 service, select the created s3 bucket ,click on properties & check the tags section:
 


5. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
