### Build the image
```shell
docker build -t 6-application-reading-environment-from-external-file .
```

If there are too many environment variables, it is convenient to put them in a file, like env.txt, and pass it to the container at run-time.
```shell
docker run --env-file=env.txt 6-application-reading-environment-from-external-file
Hola, Selva2
````
