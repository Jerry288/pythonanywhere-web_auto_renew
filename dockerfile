FROM python:3.10

ADD renewer.py .
ADD auth.json .
ADD wrapper.sh .
RUN pip install requests

RUN apt-get update -y
RUN apt-get install -y iputils-ping

CMD ["./wrapper.sh"]