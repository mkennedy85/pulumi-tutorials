import pulumi
from pulumi_docker import RemoteImage, Container

# Get a reference to the remote image "nginx:1.15.6". Without specifying the repository, the Docker provider will
# try to download it from the public Docker Hub.
image = RemoteImage("nginx-image", name="nginx", keep_locally=True)
container = Container("nginx", image=image.latest, ports=[{
    "internal": 80
}])
