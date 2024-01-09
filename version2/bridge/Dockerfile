FROM python:latest

RUN /bin/bash && apt-get update && apt-get install -y iputils-ping
RUN pip install requests
RUN pip install flask

COPY bridge.py .

CMD python ./bridge.py
