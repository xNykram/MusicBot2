FROM python:3.11.1-slim

COPY ./app /app/app

COPY ./requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

RUN apt-get upgrade & apt-get update

RUN --mount=type=cache,target=/root/.cache/ffmpeg apt-get install -y ffmpeg

ENV PYTHONPATH=/app

ENV PYTHONUNBUFFERED 1
