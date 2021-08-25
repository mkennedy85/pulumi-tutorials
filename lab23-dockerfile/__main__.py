
"""A Python Pulumi program"""

from typing import Container
import pulumi
import pulumi_docker as docker
from pulumi_docker import Image, DockerBuild
stack = pulumi.get_stack()

image_tag = stack

image = Image("my-hello",
              build=DockerBuild(context="app"),
              image_name=f"my-hello:{image_tag}",
              skip_push=True)

container = docker.Container(
    "my-hello", image=image.base_image_name, ports=[{
        "internal": 4000
    }])



