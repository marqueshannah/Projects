FROM python:3.9

RUN mkdir /code
RUN pip3 install --user redis
WORKDIR /code
RUN pip3 install --user flask==2.0.3
RUN pip3 install --user redis==4.1.4
COPY . /code

ENTRYPOINT ["python"]
CMD ["app.py"]
