# Creating ubuntu image using Docker Resource Provider. 

## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

## Prerequisites
```
pip3 install pulumi_docker

```

1. Create a directory:

    ```
    mkdir docker-ubuntu && cd docker-ubuntu
    ```

2. Create a new Pulumi project:

    ```
    pulumi new python
    
    ```
3. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.
 ```   
Previewing update (dev)

View Live: https://app.pulumi.com/kunal/docker/dev/previews/009e6910-d707-4641-b52c-84c9cc5558dd

     Type                         Name        Plan
 +   pulumi:pulumi:Stack          docker-dev  create
 +   ├─ docker:index:RemoteImage  ubuntu      create
 +   └─ docker:index:Container    ubuntu      create

Resources:
    + 3 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details

```

7. Now, run the following docker command to check the created image:

```
docker images

```
8. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
