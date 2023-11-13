FROM python:3.11.6-slim AS development

ENV APP_ENV=dev \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.6.1 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  PYTHONPATH=/app

RUN apt-get update && apt-get upgrade -y && apt-get install -y ffmpeg

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY ./app /app/app
COPY ./pyproject.toml .

RUN --mount=type=cache,target="$POETRY_CACHE_DIR" poetry install --no-interaction --no-ansi

FROM development AS production

RUN poetry install --no-interaction --no-ansi --no-dev
