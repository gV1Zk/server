FROM python:3.9

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

COPY ./django /var/www/django
WORKDIR /var/www/django

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
