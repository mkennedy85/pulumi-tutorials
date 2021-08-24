

# Create an EC2 instance & export the resource values. 

## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```
    pulumi stack init ec2-

    ```

2. Set the AWS region:

    ```
    pulumi config set aws:region ap-south-1

    ```

3. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.

    ```  
 +   ├─ aws:s3:BucketObject  favicon.png           create +   ├─ aws:s3:BucketObject  index.html            create
 +   ├─ aws:s3:BucketObject  python.png            create
 +   └─ aws:s3:BucketPolicy  bucket-policy         create

Resources:
    + 6 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details

    ```
```
4. Now, go to AWS console, navigate to S3 service & see that bucket is created.Copy the website_url as shown below & paste in the browser which show the static website:

Outputs:
```
    Outputs:
    bucket_name: "s3-website-bucket-d3c53c0"
    website_url: "http://s3-website-bucket-d3c53c0.s3-website.ap-south-1.amazonaws.com"
```

5. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
