## Passing environment variables at runtime to the image

### Building the image
```shell
docker build -t 5-application-reading-environment-var .
```

### Running the container
```shell
export name=Selva
docker run -e name 5-application-reading-environment-var  
```
The above command will pass the name/value pair `name` defined in the host machine and pass it to the docker container at runtime.
To override the value, one can do
```shell
docker run -e name=Someone 5-application-reading-environment-var  
```