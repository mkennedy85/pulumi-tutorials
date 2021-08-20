import pulumi_docker as docker

image = docker.RemoteImage("ubuntu",
                           name='ubuntu:precise'
                           )

container = docker.Container("ubuntu",
                             image=image.latest
                             )
