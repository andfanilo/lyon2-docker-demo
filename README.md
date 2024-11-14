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
docker run -v %cd%:/tmp/working -w=/tmp/working --rm -it -p 8888:8888 kaggle/python jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token="" --notebook-dir=/tmp/working

# TD
cd ./td
docker build -t td-lyon2 .
docker run td-lyon2

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