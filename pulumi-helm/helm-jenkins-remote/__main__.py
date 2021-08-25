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
