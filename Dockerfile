FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update

RUN apt-get install python-tk -y

RUN pip3 install numpy matplotlib tk

COPY . .

CMD ["python3", "main.py"]