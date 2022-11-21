FROM python:3.11

RUN apt update

WORKDIR /app

COPY requirements.txt ./

COPY .coveragerc ./

COPY ./app /app

RUN pip install -r requirements.txt

CMD ["python", "-m", "pytest", "--cov-config=.coveragerc", "--cov" ,"--cov-report=html:coverage", "tests"]
