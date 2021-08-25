[![Deploy](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook/components)

# Simple and Component-based Kubernetes Guestbook Apps

A port of the standard [Kubernetes Guestbook](https://kubernetes.io/docs/tutorials/stateless-application/guestbook/)
to Pulumi. This example shows you how to build and deploy a simple, multi-tier web application using Kubernetes and
Docker, and consists of three components:

* A single-instance Redis master to store guestbook entries
* Multiple replicated Redis instances to serve reads
* Multiple web frontend instances

In this directory, you will find two variants of the Guestbook:

1. [simple/](./simple) is a straight port of the original YAML.
2. [components](./components) demonstrates benefits of using a real language, namely eliminating boilerplate through
   the use of real component abstractions.

Both examples provision the exact same Kubernetes Guestbook application, but showcase different aspects of Pulumi.

## Deploying a Single Kubernetes YAML File

```
curl -L --remote-name https://raw.githubusercontent.com/kubernetes/examples/master/guestbook/all-in-one/guestbook-all-in-one.yaml
```
This Pulumi program uses ConfigFile to read that YAML file, provision the resources inside of it, and export the resulting IP addresses:

```
import pulumi
import pulumi_kubernetes as k8s

# Create resources from standard Kubernetes guestbook YAML example.
guestbook = k8s.yaml.ConfigFile('guestbook', 'guestbook-all-in-one.yaml')

# Export the private cluster IP address of the frontend.
frontend = guestbook.get_resource('v1/Service', 'frontend')
pulumi.export('private_ip', frontend.spec['cluster_ip'])

```


