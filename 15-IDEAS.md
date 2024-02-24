version: '3'
services:
  app1:
    build: ./app1

  app2:
    build: ./app2

  app3:
    build: ./app3
    ports:
      - "8083:8080"
    depends_on:
      - app1
      - app2

—————————

version: '3'
services:
  app1:
    build: ./app1
    volumes:
      - ./my-data:/data
  app2:
    build: ./app2
    volumes:
      - ./my-data:/data
  app3:
    build: ./app3
    volumes:
      - ./my-data:/data
    ports:
      - "8080:8080"
    depends_on:
      - app1
      - app2

—————————
version: '3'
services:
  hello:
    image: arunsundaramco70/hello
    ports:
      - "8001:8001"
    networks:
      - my_network

  upper:
    environment:
      - hello_host=hello
      - hello_port=8001
    image: arunsundaramco70/upper
    ports:
      - "8002:8001"
    networks:
      - my_network

networks:
  my_network:
    driver: bridge


—————————

Remove Stopped Containers
docker container prune

Remove Unused Images
docker image prune -a

Remove Unused Volumes
docker volume prune

Remove Unused Networks
docker network prune

All Together (not suitable for use in Production)
One can combine all of these into one command that will remove stopped containers, all unused images, all unused volumes, and all unused networks:
docker system prune --volumes


------------

import fastapi, os, uvicorn, nest_asyncio, requests, sys

app = fastapi.FastAPI()
PORT = os.environ.get('PORT', '8001')
HELLO_HOST = os.environ.get('hello_host')
HELLO_PORT = os.environ.get('hello_port')


@app.get("/upper/{text}")
def get_upper(text):
  URL = f"http://{HELLO_HOST}:{HELLO_PORT}/hello/{text}"
  print(f"{URL=}", flush=True, file=sys.stderr)
  resp = requests.get(URL) # contacts hello application
  print(resp.json(), flush=True, file=sys.stderr)
  message = resp.json()["message"]
  return {
    "text": f"{message.upper()}"
  }

nest_asyncio.apply()
uvicorn.run("main:app", host="0.0.0.0", port=PORT, log_level="error")

