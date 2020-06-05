FROM ubuntu:latest
MAINTAINER Slugin Roman 'sluginroma@yandex.ru'
RUN apt-get update -y
RUN apt-get install -y python-pip
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt
ENTRYPOINT ['python']
CMD ['app.py']