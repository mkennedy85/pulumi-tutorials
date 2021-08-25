import iam
import vpc
import utils
import pulumi
from pulumi import ResourceOptions
from pulumi_aws import eks
from pulumi_kubernetes.core.v1 import Namespace, Pod, PodSpecArgs, ContainerArgs
from pulumi_kubernetes.meta.v1 import ObjectMetaArgs, LabelSelectorArgs
from pulumi_kubernetes import Provider as KubernetesProvider
from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts, ChartOpts, FetchOpts

## EKS Cluster

eks_cluster = eks.Cluster(
    'eks-cluster',
    role_arn=iam.eks_role.arn,
    tags={
        'Name': 'pulumi-eks-cluster',
    },
    vpc_config=eks.ClusterVpcConfigArgs(
        public_access_cidrs=['0.0.0.0/0'],
        security_group_ids=[vpc.eks_security_group.id],
        subnet_ids=vpc.subnet_ids,
    ),
)

eks_node_group = eks.NodeGroup(
    'eks-node-group',
    cluster_name=eks_cluster.name,
    node_group_name='pulumi-eks-nodegroup',
    node_role_arn=iam.ec2_role.arn,
    subnet_ids=vpc.subnet_ids,
    tags={
        'Name': 'pulumi-cluster-nodeGroup',
    },
    scaling_config=eks.NodeGroupScalingConfigArgs(
        desired_size=2,
        max_size=2,
        min_size=1,
    ),
)

k8s_provider = KubernetesProvider(
    "eks-cluster", kubeconfig=utils.generate_kube_config(eks_cluster), namespace="default"
)

airflow_ns = Namespace(
    'airflow-dev',
    opts = ResourceOptions(provider=k8s_provider)
)

airflow = Chart(
    "airflow-dev",
    ChartOpts(
        chart="airflow",
        namespace=airflow_ns.metadata["name"],
        fetch_opts=FetchOpts(
            repo="https://charts.bitnami.com/bitnami",
        ),
        values={
            'web': {
                'replicaCount': 1,
            }
        }
    ),
    opts = ResourceOptions(
        providers = {
            'kubernetes': k8s_provider,
        }
    )
)

dnsutils = Pod(
    "dnsutils",
    metadata=ObjectMetaArgs(
        name="dnsutils",
        namespace="default",
    ),
    spec=PodSpecArgs(
        containers=[
            ContainerArgs(
                name="dnsutils",
                image="gcr.io/kubernetes-e2e-test-images/dnsutils:1.3",
                command=[
                    "sleep",
                    "3600",
                ],
                image_pull_policy="IfNotPresent",
            ),
        ],
        restart_policy="Always"
    ),
    opts = ResourceOptions(
        provider=k8s_provider,
    ),
)

pulumi.export('cluster-name', eks_cluster.name)
pulumi.export('kubeconfig', utils.generate_kube_config(eks_cluster))
