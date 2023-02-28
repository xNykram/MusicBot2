FROM python:3.11

RUN apt update

WORKDIR /app

COPY requirements.txt ./

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

COPY .coveragerc ./

COPY ./app /app

CMD ["python", "-m", "pytest", "--cov-config=.coveragerc", "--cov" ,"--cov-report=html:coverage", "tests"]
