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
