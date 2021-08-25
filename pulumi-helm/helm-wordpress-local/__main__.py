from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

wordpress = Chart(
    "wordpress",
    LocalChartOpts(
        path="C:/Users/kunal/pulumi-tutorials/helm-wp/wordpress",
    ),
)
