FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

COPY ./app /app/app

RUN pip install -r requirements.txt

RUN apt-get upgrade & apt-get update

RUN apt-get install -y ffmpeg
