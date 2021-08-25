# Deploying Prometheus Monitoring tool using Pulumi & Helm (using local Chart) 

## Prerequisites
```
1. A running Kubernetes Cluster.
2. kubectl cli.
3. helm package manager.
4. Add the stable repo "helm repo add stable https://charts.helm.sh/stable"

```

1. Create a directory:

    ```
    mkdir pulumi-helm-prom && cd pulumi-helm-prom
    
    ```
2. Now inside the directory "pulumi-helm-prom" run the following command to fetch prometheus repo.
```
helm fetch --untar stable/prometheus

```
2. Create a new Pulumi project:

    ```
    pulumi new kubernetes-python --force
    
    ```
3. Next, replace the contents of __main__.py file with the following code.
```
from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

prometheus = Chart(
    "prometheus",
    LocalChartOpts(
        path="prometheus",
    ),
)

```

4. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.
```
    Type                                                                   Name                                   Plan       Info         
 +   pulumi:pulumi:Stack                                                    prometheus-dev                         create...               
 +   └─ kubernetes:helm.sh/v3:Chart                                         prometheus                             create                  
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRole         prometheus-kube-state-metrics          create     warning:     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRole         prometheus-alertmanager                create     warning:     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRole         prometheus-pushgateway                 create     warning:     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRole         prometheus-server                      create     warning:     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleBinding  prometheus-kube-state-metrics          create     warning:     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleBinding  prometheus-alertmanager                create     warning:     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleBinding  prometheus-pushgateway                 create     warning:     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleBinding  prometheus-server                      create     1 warnin     
 +      ├─ kubernetes:apps/v1:DaemonSet                                     default/prometheus-node-exporter       create                  
 +      ├─ kubernetes:core/v1:ServiceAccount                                default/prometheus-kube-state-metrics  create
 +      ├─ kubernetes:core/v1:ServiceAccount                                default/prometheus-node-exporter       create                  
 +      ├─ kubernetes:core/v1:ServiceAccount                                default/prometheus-alertmanager        create
 +      ├─ kubernetes:core/v1:ConfigMap                                     default/prometheus-alertmanager        create                  
 +      ├─ kubernetes:core/v1:PersistentVolumeClaim                         default/prometheus-alertmanager        create 

 ```


5. Now, verify the status of pods running inside the kubernetes cluster by running the following command.

```
kubectl get po

```
Output:

```
NAME                                            READY   STATUS    RESTARTS   AGE
prometheus-alertmanager-74755454f6-6hp9m        2/2     Running   0          73s
prometheus-kube-state-metrics-95d956569-n2v6l   1/1     Running   0          75s
prometheus-node-exporter-bc44t                  1/1     Running   0          85sprometheus-node-exporter-kkj7q                  1/1     Running   0          85s
prometheus-pushgateway-594cd6ff6b-6gbpj         1/1     Running   0          73s
prometheus-server-7bc886d65-b8cmz               2/2     Running   0          71s

```
6. Now, check the service type, by running the following command.

```
kubectl get svc

```
Output:

```
NAME                            TYPE           CLUSTER-IP       EXTERNAL-IP                                                                PORT(S)        AGE     
kubernetes                      ClusterIP      172.20.0.1       <none>                                                                     443/TCP        43m     
prometheus-alertmanager         NodePort       172.20.183.83    <none>                                                                     80:30000/TCP   113s    
prometheus-kube-state-metrics   ClusterIP      172.20.251.27    <none>                                                                     8080/TCP       114s    
prometheus-node-exporter        ClusterIP      None             <none>                                                                     9100/TCP       113s    
prometheus-pushgateway          ClusterIP      172.20.126.209   <none>                                                                     9091/TCP       112s    
prometheus-server               LoadBalancer   172.20.24.210    aad0cd0c69b1846c8abaa67915d0a09a-1458374897.ap-south-1.elb.amazonaws.com   80:31069/TCP   112s

```
7. Copy the EXTERNAL-IP of prometheus-server, paste in the browser to see the output of prometheus server.

8. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
