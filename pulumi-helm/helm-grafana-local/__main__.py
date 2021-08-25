from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

grafana = Chart(
    "grafana",
    LocalChartOpts(
        path="grafana",
    ),
)
