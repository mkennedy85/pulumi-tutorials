# Deploying WordPress using Pulumi & Helm (using local Chart) 

## Prerequisites
```
1. A running Kubernetes Cluster.
2. kubectl cli.
3. helm package manager.
4. Add the bitnami repo "helm repo add bitnami https://charts.bitnami.com/bitnami"

```

1. Create a directory:

    ```
    mkdir pulumi-helm-wp && cd pulumi-helm-wp
    
    ```
2. Now inside the directory "pulumi-helm-wp" run the following command to fetch wordpress repo.
```
helm fetch --untar bitnami/wordpress

```
2. Create a new Pulumi project:

    ```
    pulumi new kubernetes-python --force
    
    ```
3. Next, replace the contents of __main__.py file with the following code.
```
from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

wordpress = Chart(
    "wordpress",
    LocalChartOpts(
        path="wordpress",
    ),
)


```

4. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.

```
 +   pulumi:pulumi:Stack                             helm-wp-dev                create
 +   └─ kubernetes:helm.sh/v3:Chart                  wordpress                  create
 +      ├─ kubernetes:core/v1:ServiceAccount         default/wordpress-mariadb  create
 +      ├─ kubernetes:apps/v1:StatefulSet            default/wordpress-mariadb  create
 +      ├─ kubernetes:core/v1:ConfigMap              default/wordpress-mariadb  create
 +      ├─ kubernetes:core/v1:PersistentVolumeClaim  default/wordpress          create
 +      ├─ kubernetes:core/v1:Service                default/wordpress-mariadb  create
 +      ├─ kubernetes:core/v1:Service                default/wordpress          create
 +      ├─ kubernetes:apps/v1:Deployment             default/wordpress          create
 +      ├─ kubernetes:core/v1:Secret                 default/wordpress-mariadb  create
 +      └─ kubernetes:core/v1:Secret                 default/wordpress          create

Resources:
    + 11 to create

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
NAME                        READY   STATUS    RESTARTS   AGE
wordpress-bdb6d46db-2szsx   1/1     Running   0          85s
wordpress-mariadb-0         1/1     Running   0          85s

```
6. Now, check the service type, by running the following command.

```
kubectl get svc

```
Output:

```
NAME                TYPE           CLUSTER-IP      EXTERNAL-IP                                                                PORT(S)                      AGE    
kubernetes          ClusterIP      172.20.0.1      <none>                                                                     443/TCP                      52m    wordpress           LoadBalancer   172.20.184.22   af330d6de10654c4f9b1fd7b31299326-1420330896.ap-south-1.elb.amazonaws.com   80:31740/TCP,443:31222/TCP   106s   
wordpress-mariadb   ClusterIP      172.20.51.34    <none>                                                                     3306/TCP                     106s

```
7. Copy the EXTERNAL-IP of wordpress, paste in the browser to see the output of wordpress.

8. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
