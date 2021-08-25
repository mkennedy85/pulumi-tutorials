from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

prometheus = Chart(
    "prometheus",
    LocalChartOpts(
        path="C:/Users/kunal/pulumi-tutorials/helm-prometheus/prometheus",
    ),
)
