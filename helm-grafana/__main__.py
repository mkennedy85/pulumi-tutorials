from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

grafana = Chart(
    "grafana",
    LocalChartOpts(
        path="C:/Users/kunal/pulumi-tutorials/helm-grafana/grafana",
    ),
)
