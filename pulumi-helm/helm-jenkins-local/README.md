# Deploying Jenkins server using Pulumi & Helm (using local Chart) 

## Prerequisites
```
1. A running Kubernetes Cluster.
2. kubectl cli.
3. helm package manager.
4. Add the stable repo "helm repo add stable https://charts.helm.sh/stable"

```

1. Create a directory:

    ```
    mkdir pulumi-helm-jenk && cd pulumi-helm-jenk
    
    ```
2. Now inside the directory "pulumi-helm-jenk" run the following command to fetch jenkins repo.
```
helm fetch --untar stable/jenkins

```
2. Create a new Pulumi project:

    ```
    pulumi new kubernetes-python --force
    
    ```
3. Next, replace the contents of __main__.py file with the following code.
```
from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

jenkins = Chart(
    "jenkins",
    LocalChartOpts(
        path="C:/Users/kunal/pulumi-tutorials/helm-jenkins/jenkins",
    ),
)

```

4. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.
```
Previewing update (dev)

     Type                                            Name              Plan
 +   pulumi:pulumi:Stack                             helm-jenkins-dev  create
 +   └─ kubernetes:helm.sh/v3:Chart                  jenkins           create
 +      ├─ kubernetes:core/v1:PersistentVolumeClaim  default/jenkins   create
 +      ├─ kubernetes:core/v1:Service                default/jenkins   create
 +      ├─ kubernetes:core/v1:Secret                 default/jenkins   create
 +      └─ kubernetes:apps/v1:Deployment             default/jenkins   create                                                              
 
Resources:
    + 6 to create

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
jenkins-55db64b75d-2rzkh   1/1     Running   0          109s

```

6. Now, check the service type by running the following command.
```
kubectl get svc

```
Output:

```
NAME         TYPE           CLUSTER-IP    EXTERNAL-IP                                                        PORT(S)                      AGE
jenkins      LoadBalancer   172.20.54.2   a726e074826764805977cecdb0ee7130-223577189.ap-south-1.elb.amazonaws.com   80:31071/TCP,443:31594/TCP   2m10s
kubernetes   ClusterIP      172.20.0.1    <none>                                                                    443/TCP                      36m

```

7. Copy the EXTERNAL-IP of jenkins, paste in the browser to see the output of jenkins server.

8. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
