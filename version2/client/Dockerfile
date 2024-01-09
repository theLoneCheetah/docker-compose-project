FROM python:latest

RUN /bin/bash && apt-get update && apt-get install -y iputils-ping
RUN pip install requests

COPY client.py .
