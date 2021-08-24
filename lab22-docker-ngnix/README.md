

# Creating nginx web server image using Docker Resource Provider. 

Link for tf2pulumi conversion tool https://www.pulumi.com/tf2pulumi/


## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

## Prerequisites
```
pip3 install pulumi_docker

```

1. Create a directory:

    ```
    mkdir docker-nginx && cd docker-nginx
    ```

2. Create a new Pulumi project:

    ```
    pulumi new python
    
    ```
3. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.
 ```   
Previewing update (dev)

     Type                         Name          Plan
 +   pulumi:pulumi:Stack          pul-dock-dev  create
 +   ├─ docker:index:RemoteImage  nginx-image   create
 +   └─ docker:index:Container    nginx         create

Resources:
    + 3 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details


```

7. Now, run the following docker command to check the running container:

```
docker ps

```
8. Now, check the port number (49164) as shown below.Open browser with localhost_ip:port & check the output:
```
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                                 NAMES
37228017aeab   dd34e67e3371   "/docker-entrypoint.…"   5 seconds ago    Up 5 seconds    0.0.0.0:49164->80/tcp

```
8. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
