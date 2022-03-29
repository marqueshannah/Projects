all: build run push

images:
        docker images | grep hannahmarques

ps:
        docker ps -a | grep hannahmarques

build:
        docker build -t hannahmarques/midterm2:1/0 . 

run:
        docker run -d -p 5018:5000 hannahmarques/midterm2:1.0

push:
        docker push hannahmarques/midterm2:midterm
