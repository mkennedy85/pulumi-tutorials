# Local Program

This example demonstrates adding an Automation API driver to an existing Pulumi CLI-driven program. This project sets up an automation driver in `./automation` that contains a `main.py` file that can be invoked to perform the full deployment lifecycle including automatically selecting creating/selecting stacks, setting config, update, refresh, etc. Our project layout looks like the following:

- `/aws-py-voting-app`: This is the app from the [aws-py-voting-app](https://github.com/pulumi/examples/tree/master/aws-py-voting-app) example, including the CLI-driven pulumi program.
- `/automation`: a `main.py` containing our Automation API deployment driver. This can be run like any normal python program: `python main.py`

To run this example you'll need a few pre-reqs:
1. A Pulumi CLI installation ([v3.0.0](https://www.pulumi.com/docs/get-started/install/versions/) or later)
2. The AWS CLI, with appropriate credentials.
3. Docker

First, cd into the `automation` directory and set up your virtual environment:
1. ```shell
   python3 -m venv venv
   ```
2. ```shell
   venv/bin/python3 -m pip install --upgrade pip
   ```
3. ```shell
   venv/bin/pip install -r requirements.txt
   ```

To run our automation program, run `venv/bin/python main.py`:

```shell
Chandans-MacBook-Pro:automation chandank$ venv/bin/python main.py
preparing virtual environment...
virtual environment is ready!
successfully initialized stack
setting up config
config set
refreshing stack
Refreshing (dev)

View Live: https://app.pulumi.com/kchandan/voting-app/dev/updates/3


~  docker:image:Image flask-dockerimage refreshing
~  pulumi:pulumi:Stack voting-app-dev refreshing
docker:image:Image flask-dockerimage
~  aws:iam:RolePolicyAttachment app-exec-policy refreshing
pulumi:pulumi:Stack voting-app-dev running
~  aws:ecr:Repository app-ecr-repo refreshing
~  aws:iam:RolePolicyAttachment app-access-policy refreshing
~  aws:iam:Role app-task-role refreshing
~  aws:iam:Role app-exec-role refreshing
~  aws:ecr:LifecyclePolicy app-lifecycle-policy refreshing
~  aws:ecs:TaskDefinition redis-task-definition refreshing
~  aws:ecs:Cluster app-cluster refreshing
~  aws:ec2:Vpc app-vpc refreshing
~  aws:ec2:InternetGateway app-gateway refreshing
~  aws:ec2:Subnet app-vpc-subnet refreshing
~  aws:alb:TargetGroup flask-targetgroup refreshing
~  aws:ec2:RouteTable app-routetable refreshing
~  aws:ec2:SecurityGroup security-group refreshing
~  aws:alb:TargetGroup redis-targetgroup refreshing
~  aws:ec2:MainRouteTableAssociation app_routetable_association refreshing
~  aws:alb:LoadBalancer flask-balancer refreshing
~  aws:alb:LoadBalancer redis-balancer refreshing
~  aws:alb:Listener flask-listener refreshing
~  aws:ecs:TaskDefinition flask-task-definition refreshing
~  aws:alb:Listener redis-listener refreshing
~  aws:ecs:Service redis-service refreshing
~  aws:ecs:Service flask-service refreshing
aws:iam:RolePolicyAttachment app-exec-policy
aws:iam:RolePolicyAttachment app-access-policy
aws:ecs:Cluster app-cluster
aws:ecs:TaskDefinition flask-task-definition
aws:ecs:Service redis-service
aws:ecs:Service flask-service
aws:ecr:LifecyclePolicy app-lifecycle-policy
aws:ec2:InternetGateway app-gateway
aws:ecs:TaskDefinition redis-task-definition
aws:ec2:MainRouteTableAssociation app_routetable_association
aws:ec2:RouteTable app-routetable
aws:ec2:SecurityGroup security-group
~  aws:iam:Role app-task-role updated [diff: ~managedPolicyArns]
aws:ec2:Subnet app-vpc-subnet
~  aws:iam:Role app-exec-role updated [diff: ~managedPolicyArns]
aws:alb:Listener flask-listener
aws:alb:Listener redis-listener
aws:ecr:Repository app-ecr-repo
aws:alb:TargetGroup flask-targetgroup
aws:alb:TargetGroup redis-targetgroup
~  aws:alb:LoadBalancer flask-balancer updated [diff: +dropInvalidHeaderFields,enableHttp2,idleTimeout]
~  aws:alb:LoadBalancer redis-balancer updated [diff: +dropInvalidHeaderFields,enableHttp2,idleTimeout]
~  aws:ec2:Vpc app-vpc updated [diff: ~defaultRouteTableId,mainRouteTableId]
pulumi:pulumi:Stack voting-app-dev

Outputs:
app-url: "flask-balancer-c872af2-c3c62ecffaab2393.elb.us-west-2.amazonaws.com"

Resources:
~ 5 updated
20 unchanged

Duration: 4s

refresh complete
updating stack...
Updating (dev)

View Live: https://app.pulumi.com/kchandan/voting-app/dev/updates/4


pulumi:pulumi:Stack voting-app-dev running
docker:image:Image flask-dockerimage
aws:ecs:Cluster app-cluster
aws:iam:Role app-exec-role  [diff: ~assumeRolePolicy]
aws:ec2:Vpc app-vpc
aws:iam:Role app-task-role  [diff: ~assumeRolePolicy]
aws:ecr:Repository app-ecr-repo
aws:ec2:Subnet app-vpc-subnet
aws:ec2:InternetGateway app-gateway  [diff: +__defaults]
aws:iam:RolePolicyAttachment app-exec-policy  [diff: +__defaults]
aws:ec2:SecurityGroup security-group
aws:alb:TargetGroup redis-targetgroup
aws:alb:TargetGroup flask-targetgroup
aws:ecr:LifecyclePolicy app-lifecycle-policy  [diff: +__defaults~policy]
aws:iam:RolePolicyAttachment app-access-policy  [diff: +__defaults]
aws:ecs:TaskDefinition redis-task-definition  [diff: +__defaults]
aws:alb:LoadBalancer redis-balancer
aws:ec2:RouteTable app-routetable  [diff: +__defaults~routes]
aws:alb:LoadBalancer flask-balancer
docker:image:Image flask-dockerimage  {"Client":{"Platform":{"Name":""},"CloudIntegration":"1.0.17","Version":"20.10.8","ApiVersion":"1.41","DefaultAPIVersion":"1.41","GitCommit":"3967b7d","GoVersion":"go1.16.6","Os":"darwin","Arch":"amd64","BuildTime":"Fri Jul 30 19:55:20 2021","Context":"default","Experimental":true},"Server":{"Platform":{"Name":"Docker Engine - Community"},"Components":[{"Name":"Engine","Version":"20.10.8","Details":{"ApiVersion":"1.41","Arch":"amd64","BuildTime":"Fri Jul 30 19:52:10 2021","Experimental":"false","GitCommit":"75249d8","GoVersion":"go1.16.6","KernelVersion":"5.10.47-linuxkit","MinAPIVersion":"1.12","Os":"linux"}},{"Name":"containerd","Version":"1.4.9","Details":{"GitCommit":"e25210fe30a0a703442421b0f60afac609f950a3"}},{"Name":"runc","Version":"1.0.1","Details":{"GitCommit":"v1.0.1-0-g4144b63"}},{"Name":"docker-init","Version":"0.19.0","Details":{"GitCommit":"de40ad0"}}],"Version":"20.10.8","ApiVersion":"1.41","MinAPIVersion":"1.12","GitCommit":"75249d8","GoVersion":"go1.16.6","Os":"linux","Arch":"amd64","KernelVersion":"5.10.47-linuxkit","BuildTime":"2021-07-30T19:52:10.000000000+00:00"}}
docker:image:Image flask-dockerimage  Login Succeeded
docker:image:Image flask-dockerimage  Building image './frontend'...
docker:image:Image flask-dockerimage  warning: #1 [internal] load build definition from Dockerfile
docker:image:Image flask-dockerimage  sha256:7a321d92328be9547b7d85ed77f537e53774adfab5580fc3c851d309c4ab28f2
docker:image:Image flask-dockerimage  Image build succeeded.
docker:image:Image flask-dockerimage  Pushing image '437642028138.dkr.ecr.us-west-2.amazonaws.com/app-ecr-repo-7689d56'...
docker:image:Image flask-dockerimage  The push refers to repository [437642028138.dkr.ecr.us-west-2.amazonaws.com/app-ecr-repo-7689d56]
docker:image:Image flask-dockerimage  4f7562299225: Preparing
docker:image:Image flask-dockerimage  5f2521097d34: Preparing
docker:image:Image flask-dockerimage  dc1889a6560c: Preparing
docker:image:Image flask-dockerimage  b7715857621b: Preparing
docker:image:Image flask-dockerimage  7560054c4860: Preparing
docker:image:Image flask-dockerimage  83743ed05e49: Preparing
docker:image:Image flask-dockerimage  a9ffebc5be68: Preparing
docker:image:Image flask-dockerimage  83743ed05e49: Waiting
docker:image:Image flask-dockerimage  27d9a6169c9f: Preparing
docker:image:Image flask-dockerimage  a9ffebc5be68: Waiting
docker:image:Image flask-dockerimage  27d9a6169c9f: Waiting
docker:image:Image flask-dockerimage  b9557a3d31d9: Preparing
docker:image:Image flask-dockerimage  c8f52965417f: Preparing
docker:image:Image flask-dockerimage  9cde96ca61c2: Preparing
docker:image:Image flask-dockerimage  f3fd11fd6d6c: Preparing
docker:image:Image flask-dockerimage  e553743c668b: Preparing
docker:image:Image flask-dockerimage  88af765ea71f: Preparing
docker:image:Image flask-dockerimage  b47c358499df: Preparing
docker:image:Image flask-dockerimage  cbd550635f44: Preparing
docker:image:Image flask-dockerimage  2efef025159b: Preparing
docker:image:Image flask-dockerimage  3acbf6947195: Preparing
docker:image:Image flask-dockerimage  f90fe4978ca2: Preparing
docker:image:Image flask-dockerimage  88383b8e3cb5: Preparing
docker:image:Image flask-dockerimage  b9557a3d31d9: Waiting
docker:image:Image flask-dockerimage  c8f52965417f: Waiting
docker:image:Image flask-dockerimage  9cde96ca61c2: Waiting
docker:image:Image flask-dockerimage  f3fd11fd6d6c: Waiting
docker:image:Image flask-dockerimage  e553743c668b: Waiting
docker:image:Image flask-dockerimage  88af765ea71f: Waiting
docker:image:Image flask-dockerimage  b47c358499df: Waiting
docker:image:Image flask-dockerimage  cbd550635f44: Waiting
docker:image:Image flask-dockerimage  2efef025159b: Waiting
docker:image:Image flask-dockerimage  3acbf6947195: Waiting
docker:image:Image flask-dockerimage  f90fe4978ca2: Waiting
docker:image:Image flask-dockerimage  e93627dfc607: Preparing
docker:image:Image flask-dockerimage  8f23b00cc77f: Preparing
docker:image:Image flask-dockerimage  cf691a2ea3f9: Preparing
docker:image:Image flask-dockerimage  3d3e92e98337: Preparing
docker:image:Image flask-dockerimage  8967306e673e: Preparing
docker:image:Image flask-dockerimage  9794a3b3ed45: Preparing
docker:image:Image flask-dockerimage  5f77a51ade6a: Preparing
docker:image:Image flask-dockerimage  e40d297cf5f8: Preparing
docker:image:Image flask-dockerimage  88383b8e3cb5: Waiting
docker:image:Image flask-dockerimage  e93627dfc607: Waiting
docker:image:Image flask-dockerimage  8f23b00cc77f: Waiting
docker:image:Image flask-dockerimage  cf691a2ea3f9: Waiting
docker:image:Image flask-dockerimage  3d3e92e98337: Waiting
docker:image:Image flask-dockerimage  8967306e673e: Waiting
docker:image:Image flask-dockerimage  9794a3b3ed45: Waiting
docker:image:Image flask-dockerimage  5f77a51ade6a: Waiting
docker:image:Image flask-dockerimage  e40d297cf5f8: Waiting
docker:image:Image flask-dockerimage  5f2521097d34: Layer already exists
docker:image:Image flask-dockerimage  dc1889a6560c: Layer already exists
docker:image:Image flask-dockerimage  7560054c4860: Layer already exists
docker:image:Image flask-dockerimage  4f7562299225: Layer already exists
docker:image:Image flask-dockerimage  b7715857621b: Layer already exists
docker:image:Image flask-dockerimage  83743ed05e49: Layer already exists
docker:image:Image flask-dockerimage  a9ffebc5be68: Layer already exists
docker:image:Image flask-dockerimage  27d9a6169c9f: Layer already exists
docker:image:Image flask-dockerimage  c8f52965417f: Layer already exists
docker:image:Image flask-dockerimage  b9557a3d31d9: Layer already exists
docker:image:Image flask-dockerimage  9cde96ca61c2: Layer already exists
docker:image:Image flask-dockerimage  f3fd11fd6d6c: Layer already exists
docker:image:Image flask-dockerimage  e553743c668b: Layer already exists
docker:image:Image flask-dockerimage  88af765ea71f: Layer already exists
docker:image:Image flask-dockerimage  b47c358499df: Layer already exists
docker:image:Image flask-dockerimage  cbd550635f44: Layer already exists
docker:image:Image flask-dockerimage  2efef025159b: Layer already exists
docker:image:Image flask-dockerimage  f90fe4978ca2: Layer already exists
docker:image:Image flask-dockerimage  3acbf6947195: Layer already exists
docker:image:Image flask-dockerimage  88383b8e3cb5: Layer already exists
docker:image:Image flask-dockerimage  e93627dfc607: Layer already exists
docker:image:Image flask-dockerimage  cf691a2ea3f9: Layer already exists
docker:image:Image flask-dockerimage  3d3e92e98337: Layer already exists
docker:image:Image flask-dockerimage  8f23b00cc77f: Layer already exists
docker:image:Image flask-dockerimage  8967306e673e: Layer already exists
docker:image:Image flask-dockerimage  9794a3b3ed45: Layer already exists
docker:image:Image flask-dockerimage  e40d297cf5f8: Layer already exists
docker:image:Image flask-dockerimage  5f77a51ade6a: Layer already exists
docker:image:Image flask-dockerimage  7a321d92328be9547b7d85ed77f537e53774adfab5580fc3c851d309c4ab28f2: digest: sha256:ca7507ca038ff3eade6d795c5f409577a12f3208c9bdf096229c04ef0f274903 size: 6175
docker:image:Image flask-dockerimage  Using default tag: latest
docker:image:Image flask-dockerimage  The push refers to repository [437642028138.dkr.ecr.us-west-2.amazonaws.com/app-ecr-repo-7689d56]
docker:image:Image flask-dockerimage  4f7562299225: Preparing
docker:image:Image flask-dockerimage  5f2521097d34: Preparing
docker:image:Image flask-dockerimage  dc1889a6560c: Preparing
docker:image:Image flask-dockerimage  b7715857621b: Preparing
docker:image:Image flask-dockerimage  7560054c4860: Preparing
docker:image:Image flask-dockerimage  83743ed05e49: Preparing
docker:image:Image flask-dockerimage  a9ffebc5be68: Preparing
docker:image:Image flask-dockerimage  27d9a6169c9f: Preparing
docker:image:Image flask-dockerimage  b9557a3d31d9: Preparing
docker:image:Image flask-dockerimage  c8f52965417f: Preparing
docker:image:Image flask-dockerimage  9cde96ca61c2: Preparing
docker:image:Image flask-dockerimage  f3fd11fd6d6c: Preparing
docker:image:Image flask-dockerimage  83743ed05e49: Waiting
docker:image:Image flask-dockerimage  a9ffebc5be68: Waiting
docker:image:Image flask-dockerimage  27d9a6169c9f: Waiting
docker:image:Image flask-dockerimage  b9557a3d31d9: Waiting
docker:image:Image flask-dockerimage  c8f52965417f: Waiting
docker:image:Image flask-dockerimage  9cde96ca61c2: Waiting
docker:image:Image flask-dockerimage  e553743c668b: Preparing
docker:image:Image flask-dockerimage  88af765ea71f: Preparing
docker:image:Image flask-dockerimage  b47c358499df: Preparing
docker:image:Image flask-dockerimage  cbd550635f44: Preparing
docker:image:Image flask-dockerimage  2efef025159b: Preparing
docker:image:Image flask-dockerimage  3acbf6947195: Preparing
docker:image:Image flask-dockerimage  f90fe4978ca2: Preparing
docker:image:Image flask-dockerimage  88383b8e3cb5: Preparing
docker:image:Image flask-dockerimage  e93627dfc607: Preparing
docker:image:Image flask-dockerimage  8f23b00cc77f: Preparing
docker:image:Image flask-dockerimage  cf691a2ea3f9: Preparing
docker:image:Image flask-dockerimage  f3fd11fd6d6c: Waiting
docker:image:Image flask-dockerimage  3d3e92e98337: Preparing
docker:image:Image flask-dockerimage  8967306e673e: Preparing
docker:image:Image flask-dockerimage  9794a3b3ed45: Preparing
docker:image:Image flask-dockerimage  5f77a51ade6a: Preparing
docker:image:Image flask-dockerimage  e40d297cf5f8: Preparing
docker:image:Image flask-dockerimage  3acbf6947195: Waiting
docker:image:Image flask-dockerimage  f90fe4978ca2: Waiting
docker:image:Image flask-dockerimage  e553743c668b: Waiting
docker:image:Image flask-dockerimage  88af765ea71f: Waiting
docker:image:Image flask-dockerimage  b47c358499df: Waiting
docker:image:Image flask-dockerimage  88383b8e3cb5: Waiting
docker:image:Image flask-dockerimage  e93627dfc607: Waiting
docker:image:Image flask-dockerimage  8f23b00cc77f: Waiting
docker:image:Image flask-dockerimage  cbd550635f44: Waiting
docker:image:Image flask-dockerimage  2efef025159b: Waiting
docker:image:Image flask-dockerimage  cf691a2ea3f9: Waiting
docker:image:Image flask-dockerimage  3d3e92e98337: Waiting
docker:image:Image flask-dockerimage  8967306e673e: Waiting
docker:image:Image flask-dockerimage  9794a3b3ed45: Waiting
docker:image:Image flask-dockerimage  5f77a51ade6a: Waiting
docker:image:Image flask-dockerimage  e40d297cf5f8: Waiting
docker:image:Image flask-dockerimage  dc1889a6560c: Layer already exists
docker:image:Image flask-dockerimage  7560054c4860: Layer already exists
docker:image:Image flask-dockerimage  5f2521097d34: Layer already exists
docker:image:Image flask-dockerimage  b7715857621b: Layer already exists
docker:image:Image flask-dockerimage  4f7562299225: Layer already exists
docker:image:Image flask-dockerimage  83743ed05e49: Layer already exists
docker:image:Image flask-dockerimage  a9ffebc5be68: Layer already exists
docker:image:Image flask-dockerimage  27d9a6169c9f: Layer already exists
docker:image:Image flask-dockerimage  b9557a3d31d9: Layer already exists
docker:image:Image flask-dockerimage  c8f52965417f: Layer already exists
docker:image:Image flask-dockerimage  9cde96ca61c2: Layer already exists
docker:image:Image flask-dockerimage  f3fd11fd6d6c: Layer already exists
docker:image:Image flask-dockerimage  e553743c668b: Layer already exists
docker:image:Image flask-dockerimage  88af765ea71f: Layer already exists
docker:image:Image flask-dockerimage  b47c358499df: Layer already exists
docker:image:Image flask-dockerimage  cbd550635f44: Layer already exists
docker:image:Image flask-dockerimage  2efef025159b: Layer already exists
docker:image:Image flask-dockerimage  f90fe4978ca2: Layer already exists
docker:image:Image flask-dockerimage  3acbf6947195: Layer already exists
docker:image:Image flask-dockerimage  88383b8e3cb5: Layer already exists
docker:image:Image flask-dockerimage  8f23b00cc77f: Layer already exists
docker:image:Image flask-dockerimage  e93627dfc607: Layer already exists
docker:image:Image flask-dockerimage  cf691a2ea3f9: Layer already exists
docker:image:Image flask-dockerimage  3d3e92e98337: Layer already exists
docker:image:Image flask-dockerimage  8967306e673e: Layer already exists
docker:image:Image flask-dockerimage  9794a3b3ed45: Layer already exists
docker:image:Image flask-dockerimage  5f77a51ade6a: Layer already exists
docker:image:Image flask-dockerimage  e40d297cf5f8: Layer already exists
docker:image:Image flask-dockerimage  latest: digest: sha256:ca7507ca038ff3eade6d795c5f409577a12f3208c9bdf096229c04ef0f274903 size: 6175
docker:image:Image flask-dockerimage  Image push succeeded.
aws:ec2:MainRouteTableAssociation app_routetable_association  [diff: +__defaults]
aws:alb:Listener redis-listener  [diff: +__defaults~defaultActions]
aws:alb:Listener flask-listener  [diff: +__defaults~defaultActions]
aws:ecs:TaskDefinition flask-task-definition  [diff: +__defaults]
aws:ecs:Service redis-service  [diff: ~loadBalancers,networkConfiguration]
aws:ecs:Service flask-service  [diff: ~loadBalancers,networkConfiguration]
pulumi:pulumi:Stack voting-app-dev

Diagnostics:
docker:image:Image (flask-dockerimage):
warning: #1 [internal] load build definition from Dockerfile
#1 sha256:77b0ae9fd21e4c9bfd5ea8fd9b1de97cb286c5b7c9681540f00dfbb3acac25b5
#1 transferring dockerfile: 122B 0.0s done
#1 DONE 0.0s

#2 [internal] load .dockerignore
#2 sha256:b4eacecbcc6e145f266aa2ae9bb5aac998a057dca184b75e319ac3fd2502b1ce
#2 transferring context: 2B done
#2 DONE 0.0s

#3 [internal] load metadata for docker.io/tiangolo/uwsgi-nginx-flask:python3.6
#3 sha256:0c2fa23bcb11452f95b5b29eb37f2d2bf90f1bc8956bd39d202248798f27ffd9
#3 DONE 0.7s

#4 [1/3] FROM docker.io/tiangolo/uwsgi-nginx-flask:python3.6@sha256:98c838b9d7861245ca4035816e8deb0f4efa11bc5deb8bdd74df0ec0b2aa5836
#4 sha256:fb0e756144bb81a8b46d7c2c376c1f3fbc0fa0b273eaa09f5af61768fc83ca93
#4 DONE 0.0s

#6 [internal] load build context
#6 sha256:207ada1332ee38ef720699abf1137916b96b5f7f7c00153b54eb39b237f1d74c
#6 transferring context: 5.34kB 0.0s done
#6 DONE 0.0s

#5 [2/3] RUN  pip install redis
#5 sha256:45bba08ebebb5c1b258fddf51df2c571539058099c122c1d6255bbd5c1481cd5
#5 CACHED

#7 [3/3] COPY /app /app
#7 sha256:f242416d7ceaf4442315752df9d689ca7041b0f05677c09d150d44b9d899111a
#7 CACHED

#8 exporting to image
#8 sha256:e8c613e07b0b7ff33893b694f7759a10d42e180f2b4dc349fb57dc6b71dcab00
#8 exporting layers done
#8 writing image sha256:7a321d92328be9547b7d85ed77f537e53774adfab5580fc3c851d309c4ab28f2 done
#8 naming to 437642028138.dkr.ecr.us-west-2.amazonaws.com/app-ecr-repo-7689d56 done
#8 DONE 0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them

Outputs:
app-url: "flask-balancer-c872af2-c3c62ecffaab2393.elb.us-west-2.amazonaws.com"

Resources:
25 unchanged

Duration: 17s

update summary:
{
    "same": 25
}
app url: flask-balancer-c872af2-c3c62ecffaab2393.elb.us-west-2.amazonaws.com
Chandans-MacBook-Pro:automation chandank$```

To destroy our stack, we run our automation program with an additional `destroy` argument:

```shell
```
