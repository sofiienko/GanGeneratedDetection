FROM tensorflow/tensorflow:latest

COPY requirements.txt /flask-deployment/requirements.txt

WORKDIR /flask-deployment

RUN pip install -r requirements.txt

COPY . /flask-deployment

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["server.py"]