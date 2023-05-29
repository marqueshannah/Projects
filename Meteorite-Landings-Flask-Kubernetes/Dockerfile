FROM centos:7.9.2009

RUN yum update -y && \
    yum install -y python3

RUN pip3 install Flask==2.0.3 \
                  redis==4.1.4

COPY ML_Data_Sample.json /data/ML_Data_Sample.json
COPY app.py /data/app.py

WORKDIR /data/

ENTRYPOINT ["python3"]

CMD ["app.py"]
