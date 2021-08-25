

# Stateless Application Using a Deployment

A version of the [Kubernetes Stateless Application Deployment](
https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/) example that uses Pulumi.
This example deploys a replicated Nginx server to a Kubernetes cluster, using Python and no YAML.

There is an [interactive Tutorial available](https://www.pulumi.com/docs/tutorials/kubernetes/stateless-app/) for
this example. If this is your first time using Pulumi for Kubernetes, we recommend starting there.

## Pre-Requisites

Install Pulumi
```
brew install pulumi
```
Install Kubectl on MacOS

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"
```

You should already have k8s cluster created and kubectl configured ( if you have pulumi to install eks then use below command

```
aws eks --region us-east-2 update-kubeconfig --name $(pulumi stack output cluster-name)
```
Or 

The environment variable: $KUBECONFIG,
Or in current user’s default kubeconfig directory: ~/.kube/config


## Running the App

After cloning this repo, `cd` into this directory and create a new stack, a logical deployment target that we'll deploy into:

```bash
    $ pulumi stack init dev
```

Now to perform the deployment, simply run `pulumi up`. It will first show you a preview of what will take place.
After confirming, the deployment will take place in approximately 20 seconds:

```bash
    $ pulumi up -y
    Previewing update (dev):
        Type                           Name                     Plan       
    +   pulumi:pulumi:Stack            kubernetes-py-nginx-dev  create     
    +   └─ kubernetes:apps:Deployment  nginx-deployment         create     
    
    Resources:
        + 2 to create

    Do you want to perform this update? yes
    Updating (dev):
        Type                           Name                     Status      
    +   pulumi:pulumi:Stack            kubernetes-py-nginx-dev  created     
    +   └─ kubernetes:apps:Deployment  nginx-deployment         created     
    
    Outputs:
        nginx: "nginx-deployment-ts0qpwi9"

    Resources:
        + 2 created

    Duration: 10s
```

This deployment is now running, and you can run commands like `kubectl get pods` to see the application's resources.

The stack's replica count is configurable. By default, it will scale up to three instances, but we can easily change
that to five, by running the `pulumi config` command followed by another `pulumi up`:

```bash
    $ pulumi config set replicas 5
    $ pulumi up -y
    Previewing update (dev):
        Type                           Name                     Plan       Info
        pulumi:pulumi:Stack            kubernetes-py-nginx-dev             
    ~   └─ kubernetes:apps:Deployment  nginx-deployment         update     [diff: ~spec]
    
    Resources:
        ~ 1 to update
        1 unchanged

    Updating (dev):
        Type                           Name                     Status      Info
        pulumi:pulumi:Stack            kubernetes-py-nginx-dev              
    ~   └─ kubernetes:apps:Deployment  nginx-deployment         updated     [diff: ~spec]
    
    Outputs:
        nginx: "nginx-deployment-ts0qpwi9"

    Resources:
        ~ 1 updated
        1 unchanged

    Duration: 15s
```

After we're done, we can tear down all resources, including removing our stack, with a couple commands:

```bash
    $ pulumi destroy --yes
    $ pulumi stack rm --yes
```
