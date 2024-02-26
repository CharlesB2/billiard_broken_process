FROM python:3.10-alpine

WORKDIR /app
COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv
RUN pipenv install --system

COPY . /app
