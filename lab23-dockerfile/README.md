

# Creating python hello world app using Dockerfile. 



## Deploying and running the program



## Prerequisites
```
source venv/bin/activate && pip3 install pulumi_docker

```

    ```
Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.
 ```   
Previewing update (dev)

View Live: https://app.pulumi.com/kunal/test-demo/dev/previews/97331a36-3135-4dfd-bc45-66b9fc488444

     Type                       Name           Plan
 +   pulumi:pulumi:Stack        test-demo-dev  create
 +   ├─ docker:image:Image      my-hello       create
 +   └─ docker:index:Container  my-hello       create

Resources:
    + 3 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details

```

Now, run the following docker command to check the running container:

```
docker ps

```
Check the port number (49165) as shown below.Open browser with localhost_ip:port & check the output:
```
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS             PORTS                                                 NAMES
4a759c0490fb   my-hello:dev   "python /app/__main_…"   7 seconds ago       Up 7 seconds       0.0.0.0:49165->4000/tcp                               my-hello-638dfad

```
To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
