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
docker run -it --rm --name python-test python:3.10 ipython

docker build -t ipython-fan .
docker run -it --rm ipython-fan ipython
```