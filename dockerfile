FROM python:3.10

ADD renewer.py .
ADD auth.json .

RUN apt-get update -y
RUN apt-get install -y iputils-ping

CMD ["python", "renewer.py"]