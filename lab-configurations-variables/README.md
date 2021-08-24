

# Create an S3 bucket by configuring region, bucket_name. 

## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```
    pulumi stack init s3-config

    ```

2. Set the AWS region:

    ```
    pulumi config set aws:region ap-south-1
    pulumi config set s3-project:bucket_name s3-kk
    pulumi config set --secret dbPassword admin@123

    ```

3. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.
 ```  
Previewing update (s3-config)

     Type                 Name                  Plan       Info
 +   pulumi:pulumi:Stack  s3-project-s3-config  create     2 messages
 +   └─ aws:s3:Bucket     s3-kks3-config        create
 Diagnostics:
  pulumi:pulumi:Stack (s3-project-s3-config):
    Region ap-south-1
    Password: [secret]
 
Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details    
```
4. Now, go to AWS console, navigate to S3 service & see that bucket is created:
Outputs:

```
    bucket_name: "s3-kks3-config-86d9fbc"
   
```

5. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
