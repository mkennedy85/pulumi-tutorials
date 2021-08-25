# Deploying Jenkins server using Pulumi & Helm (using Remote Chart) 

## Prerequisites
```
1. A running Kubernetes Cluster.
2. kubectl cli.
3. helm package manager.

```

1. Create a directory:

    ```
    mkdir pulumi-helm-jenkins && cd pulumi-helm-jenkins
    ```

2. Create a new Pulumi project:

    ```
    pulumi new kubernetes-python
    
    ```
3. Next, replace the contents of __main__.py file with the following code.
```
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts

jenkins = Chart(
    "jenkins",
    ChartOpts(
        chart="jenkins",
        version="8.0.9",
        fetch_opts=FetchOpts(
            repo="https://charts.bitnami.com/bitnami",
        ),
    ),
)

```

4. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.



5. Now, verify the status of pods running inside the kubernetes cluster by running the following command.
```
kubectl get po

```
6. Now, check the service type, by running the following command.
```
kubectl get svc

```
7. Copy the external dns name & paste in the browser to see the output of jenkins server.

8. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
