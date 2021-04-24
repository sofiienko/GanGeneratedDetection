FROM tensorflow/tensorflow:latest

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

COPY requirements.txt /flask-deployment/requirements.txt

WORKDIR /flask-deployment

RUN pip install -r requirements.txt

COPY . /flask-deployment

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["server.py"]