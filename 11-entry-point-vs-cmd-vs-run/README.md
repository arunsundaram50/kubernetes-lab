# Note:
- ENTRYPOINT and CMD does not create a layer, is meant to run commands at the container runtime
- RUN creates a layer and is meant for installing and running other commands during image creation

## Case #1
CMD ["./hello.py"]

### Run options:
```bash
docker run image_name 
```
Outputs: 
```bash
Hello, name
./hello.py
```

```bash
docker run image_name echo 2 3
```

Outputs: 
```bash
2 3
```


## Case #2
ENTRYPOINT ["./hello.py"]
CMD ["1"]
### Run options:
```bash
docker run image_name 
```
Output:
```bash
Hello, name
./hello.py
1
````

``bash
docker run image_name echo 2 3
```

Output:
```bash
Hello, name
./hello.py
echo
2
3
```
