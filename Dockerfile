FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app 

RUN pip3 install -r requirements.txt

ENV FLASK_APP flaskr
ENV FLASK_ENV development
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
