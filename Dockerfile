FROM python:3.8.3-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_NO_CACHE_DIR=off

ARG POETRY_VERSION
ENV POETRY_VERSION=${POETRY_VERSION:-1.0.5}

RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false

WORKDIR /srv

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root --no-ansi --no-interaction

COPY exercises/ exercises/
COPY tests/ tests/
COPY pytest.ini .

CMD ["python", "-m", "main.py"]
