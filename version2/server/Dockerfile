FROM python:latest

RUN /bin/bash && apt-get update && apt-get install -y iputils-ping
RUN pip install flask

COPY server.py .
COPY hello.html ./templates/
