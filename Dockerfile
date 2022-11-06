FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

COPY ./app /app

RUN pip install -r requirements.txt
