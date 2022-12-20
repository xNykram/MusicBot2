FROM python:3.11

WORKDIR /app

COPY /app .

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

RUN pip install -r requirements.txt

RUN apt-get upgrade & apt-get update

RUN apt-get install -y ffmpeg
