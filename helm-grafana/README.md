# Deploying Grafana tool using Pulumi & Helm (using local Chart) 

## Prerequisites
```
1. A running Kubernetes Cluster.
2. kubectl cli.
3. helm package manager.
4. Add the stable repo "helm repo add stable https://charts.helm.sh/stable"

```

1. Create a directory:

    ```
    mkdir pulumi-helm-graf && cd pulumi-helm-graf
    
    ```
2. Now inside the directory "pulumi-helm-graf" run the following command to fetch grafana repo.
```
helm fetch --untar stable/grafana

```
2. Create a new Pulumi project:

    ```
    pulumi new kubernetes-python --force
    
    ```
3. Next, replace the contents of __main__.py file with the following code.
```
from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

grafana = Chart(
    "grafana",
    LocalChartOpts(
        path="C:/Users/kunal/pulumi-tutorials/helm-grafana/grafana",
    ),
)

```

4. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.
```
Previewing update (dev)

     Type                                            Name                     Plan
 +   pulumi:pulumi:Stack                             helm-grafana-dev         create
 +   └─ kubernetes:helm.sh/v3:Chart                  grafana                  create
 +      ├─ kubernetes:core/v1:ServiceAccount         default/grafana          create
 +      ├─ kubernetes:core/v1:PersistentVolumeClaim  default/grafana          create
 +      ├─ kubernetes:core/v1:ConfigMap              default/grafana-envvars  create
 +      ├─ kubernetes:core/v1:Service                default/grafana          create
 +      ├─ kubernetes:apps/v1:Deployment             default/grafana          create
 +      └─ kubernetes:core/v1:Secret                 default/grafana-admin    create

Resources:
    + 8 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details

```

5. Now, verify the status of pods running inside the kubernetes cluster by running the following command.
```
kubectl get po

```
Output
```
NAME                       READY   STATUS    RESTARTS   AGE
grafana-5d79dc5fdb-4gzgp   1/1     Running   0          66s

```
6. Now, check the service type, by running the following command.
```
kubectl get svc

```
Output
```
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP                                                              PORT(S)          AGE
grafana      LoadBalancer   172.20.252.185   a0c87dc38c7a1451cb83c67df0f60244-58193903.ap-south-1.elb.amazonaws.com   3000:31167/TCP   118s
kubernetes   ClusterIP      172.20.0.1       <none>                                                                   443/TCP          29m

```
7. Copy the EXTERNAL-IP of grafana, paste in the browser with port no 3000 to see the output of grafana server.

8. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
