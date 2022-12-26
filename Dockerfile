FROM python:3.11.1-slim

WORKDIR /app

COPY /app .

COPY ./requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

RUN apt-get upgrade & apt-get update

RUN apt-get install -y ffmpeg
