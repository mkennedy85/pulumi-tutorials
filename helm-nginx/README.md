# Deploying nginx web server using Pulumi & Helm (using Remote Chart) 

## Prerequisites

```
1. A running Kubernetes Cluster.
2. kubectl cli.
3. helm package manager.

```

1. Create a directory:

    ```
    mkdir pulumi-helm-ng && cd pulumi-helm-ng

    ```

2. Create a new Pulumi project:

    ```
    pulumi new kubernetes-python
    
    ```
3. Next, replace the contents of __main__.py file with the following code.
```
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts

nginx = Chart(
    "nginx",
    ChartOpts(
        chart="nginx",
        version="9.5.0",
        fetch_opts=FetchOpts(
            repo="https://charts.bitnami.com/bitnami",
        ),
    ),
)

```

4. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.

```
      Type                                 Name                Plan
 +   pulumi:pulumi:Stack                  helm-nginx-dev      create
 +   └─ kubernetes:helm.sh/v3:Chart       nginx               create
 +      ├─ kubernetes:core/v1:ConfigMap   nginx-server-block  create
 +      ├─ kubernetes:core/v1:Service     nginx               create
 +      └─ kubernetes:apps/v1:Deployment  nginx               create
 
Resources:
    + 5 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details  
    
```

5. Now, verify the status of pods running inside the kubernetes cluster by running the following command.

```
kubectl get po

```
Output:

```
NAME                    READY   STATUS    RESTARTS   AGE
nginx-c667f8dbd-lrbtd   1/1     Running   0          2m10s

```
6. Now, check the service type, by running the following command.

```
kubectl get svc

```
Output:

```
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP                                                                PORT(S)        AGE
kubernetes   ClusterIP      172.20.0.1       <none>                                                                     443/TCP        73m
nginx        LoadBalancer   172.20.157.248   aefe4d79ff36a4b319b82345f7db4de7-1068677355.ap-south-1.elb.amazonaws.com   80:31539/TCP   32s                                                                      

```
7. Copy the EXTERNAL-IP of nginx, paste in the browser to see the output of nginx web server.

8. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
