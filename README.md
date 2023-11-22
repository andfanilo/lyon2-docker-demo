# Docker Demo

Explaining Docker to my students, step by step

```sh
docker version
docker compose version

docker run hello-world
docker images
docker ps
docker ps -a
docker rm $id

docker pull python:3.10
# head to https://hub.docker.com/ 
docker run -it --rm --name python-test python:3.10 python

# client Docker file
cd ./client
docker build -t mlops-client:latest .
docker run -p 8501:8501 --rm mlops-client:latest

# server Docker file
cd ./server
docker build -t mlops-server:latest .
docker run -p 8000:8000 --rm mlops-server:latest

docker compose up --build
```