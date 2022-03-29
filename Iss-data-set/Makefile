all: build run push

images:
        docker images | grep hannahmarques

ps:
        docker ps -a | grep hannahmarques

build:
        docker build -t hannahmarques/flask-iss-work:midterm .

run:
        docker run -d -p 5018:5000 hannahmarques/flask-iss-work:midterm

push:
        docker push hannahmarques/flask-iss-work:midterm
