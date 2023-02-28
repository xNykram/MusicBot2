FROM python:3.11.1-slim

COPY ../../app /app/app

COPY ../../pyproject.toml .


ENV APP_ENV=prod \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.3.2 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  PYTHONPATH=/app

RUN --mount=type=cache,target="$POETRY_CACHE_DIR" pip install "poetry==$POETRY_VERSION"

RUN --mount=type=cache,target="$POETRY_CACHE_DIR" \
    poetry install \
    $(if [ "$APP_ENV" = "prod" ]; then echo '--only main'; fi) \
    --no-interaction --no-ansi

RUN apt-get upgrade & apt-get update

RUN --mount=type=cache,target=/root/.cache/ffmpeg apt-get install -y ffmpeg
