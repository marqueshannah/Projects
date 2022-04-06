# DATABASES: working with Redis and Flask

## Description :
This assignment allows the developer to work with the Flask application, while utilizing a database that allows it to be accessed from different computers. 
This program runs and retrieves data from the database.

## How to Launch the Redis:
Log in into your ISP server and type into the command line: `docker run -v $(pwd)/data:/data -p <flask port>:6379 -d --name <name>-redis redis:6 --save 1 1 `
Make sure to add -d flag to lauch it in the background. 

## How to Pull/Build/Launch Flask App:
Create a Dockerfile with the following:

FROM python:3.9

``` 
RUN mkdir /app
RUN pip3 install --user redis
WORKDIR /code
RUN pip3 install --user flask=2.0.3
RUN pip3 install --user redis==4.1.4
COPY . /code

ENTRYPOINT ["python"]
CMD ["app.py"]
```

Build the container by typing in command line: 
`docker build -t <username>/<file-name>:<name> . `
Push the container typing in command line:
`docker push <username>/<file-name>:<name>`
To pull type: 
`docker pull <username>/<file-name>:<name>`

Then, to launch and interact with the Flask application, type and run in command line:

`export FLASK_APP=app.py`

`export FLASK_ENV=development`

`flask run -p <flask port #>`

Instructions to Perform POST and GET Requests to Flask App:

### Open a separate temrinal and do the following:

Type in command line: 

`curl localhost:<flask port>/data -X POST`

This command loads the Meteorite Landings data and outputs if it has been read successfully. 

Type in command line: 

`curl localhost:<flask port>/data`

This command reads the data out of Redis and returns it as a JSON list.
