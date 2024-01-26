We need to use CACHEBUST like
```
COPY config.txt /tmp/${CACHEBUST}.txt
```
Any command  that appear after it will not use cache if the value of CACHEBUST is different from previous times. One consistent way of ensuring CACHEBUST value is different is to use `date +%s` like so:

```shell
ARG CACHEBUST=1
--build-arg CACHEBUST=$(date +%s)
docker build --build-arg="CACHEBUST=$(date +%s)" -t 10-cache-busting .

# OTHER COMMANDS

```

The main use is to make docker ignore all cached layers (for debugging docker builds)

