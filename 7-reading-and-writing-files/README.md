
## run
### The following command will run the default `CMD [ "./increment.py" ]` in the `Dockerfile`
```shell
docker run 7-reading-and-writing-files
```
### This will run the user-specified command (in this case `/bin/sh`) and not the default `CMD`
```shell
docker run -it 7-reading-and-writing-files /bin/sh
```

## exec
### exec runs a command in a running container
```shell
docker exec -it <CONTAINER_ID> /bin/sh
```
### To get the ID/name of the running container
```shell
docker container ls
```

## attach
Attaches the stdin and stdout of the running container to an interactive session so that we can enter some input and see the output. Note: if there is already an interactive session, the input/output will be mirrored across all sessions.
For example:
Enter this in one terminal
```shell
docker run -it 7-reading-and-writing-files ./increment.py
```
And this in another
```shell
docker attach <CONTANER_ID>
```


## Questions

### How to verify the contents of a file in the image after execution?
To run an interactive session to examine the contents of the image
```shell
docker run -it 7-reading-and-writing-files /bin/sh
```

### How to push the result to an external file?
```shell
docker exec -it <CONTAINER_ID> cat /number.txt > x.txt
```
`cat` outputs the content to stdout which "we" capture using ">" into `x.txt`

```shell
docker cp <CONTAINER_ID>:/number.txt y.txt
```
The `cp` is a Docker command

#### Why this won't work
```shell
docker exec -it <CONTAINER_ID> cp /number.txt x.txt
```
because `cp` is a shell command that runs inside the container, it creates x.txt inside the container
