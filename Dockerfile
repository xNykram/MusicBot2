FROM python:3.11

WORKDIR /app

COPY /app /app/app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get upgrade & apt-get update

RUN apt-get install -y ffmpeg
