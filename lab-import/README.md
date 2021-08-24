
## Import an existing s3 bucket into Pulumi

This example imports an existing AWS S3 bucket named company-infra-logs and defines the resource name for your Pulumi program as infra-logs:

Your Pulumi stack must be configured correctly—e.g., using the same AWS region as the resource you’re importing—otherwise the resource will not be found.

```
pulumi import aws:s3/bucket:Bucket infra-logs company-infra-logs


     Type                 Name             Plan
 +   pulumi:pulumi:Stack  import-post-dev  create
 =   └─ aws:s3:Bucket     infra-logs       import

Resources:
    + 1 to create
    = 1 to import
    2 changes
```
