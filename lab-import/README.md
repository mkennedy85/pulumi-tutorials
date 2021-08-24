
When working with existing resources, there are two primary scenarios:

You need to reference existing resources to use as inputs to new resources in Pulumi
You need to adopt existing resources under management so they can be managed by Pulumi

```
pulumi import aws:s3/bucket:Bucket pulumi-imported-example pulumi-import-example
```
