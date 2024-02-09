## Create a volume
```bash
docker plugin install --grant-all-permissions vieux/sshfs
docker volume create --driver vieux/sshfs \
  -o sshcmd=asundaram@home-server:/home/asundaram \
  home-server-volume
```
### Use the volume
```bash
docker run --rm -d \
  --name arun-container \
  --mount type=volume,src=home-server-volume,target=/home-server/data,volume-opt=password=testpassword \
  11-entry-point-vs-cmd-vs-run
```




## Volumes
- runtime: docker run image_name -v /local/path1:/image/path1 -v /local/path2:/image/path2
- runtime: docker run image_name --mount /local/path1:/image/path1
- Dockerfile: volume
