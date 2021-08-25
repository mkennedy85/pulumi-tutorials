from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

jenkins = Chart(
    "jenkins",
    LocalChartOpts(
        path="C:/Users/kunal/pulumi-tutorials/helm-jenkins/jenkins",
    ),
)
