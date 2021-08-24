
## Import an existing s3 bucket into Pulumi

This example imports an existing AWS S3 bucket named company-infra-logs and defines the resource name for your Pulumi program as infra-logs:

Your Pulumi stack must be configured correctly—e.g., using the same AWS region as the resource you’re importing—otherwise the resource will not be found.

```
$ pulumi import aws:s3/bucket:Bucket pulumi-imported ck-pulumi-import
Previewing import (import-vpc)

View Live: https://app.pulumi.com/becloudready/s3-project/import-vpc/previews/8970ab14-719a-4f94-8976-969e5c4dd9b9

     Type                 Name                   Plan       
 +   pulumi:pulumi:Stack  s3-project-import-vpc  create     
 =   └─ aws:s3:Bucket     pulumi-imported        import     
 
Resources:
    + 1 to create
    = 1 to import
    2 changes

Do you want to perform this import? yes
Importing (import-vpc)

View Live: https://app.pulumi.com/becloudready/s3-project/import-vpc/updates/1

     Type                 Name                   Status       
 +   pulumi:pulumi:Stack  s3-project-import-vpc  created      
 =   └─ aws:s3:Bucket     pulumi-imported        imported     
 
Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 3s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

import pulumi
import pulumi_aws as aws

pulumi_imported = aws.s3.Bucket("pulumi-imported",
    acl="private",
    bucket="ck-pulumi-import",
    force_destroy=False,
    opts=pulumi.ResourceOptions(protect=True))
$ pulumi update
```
