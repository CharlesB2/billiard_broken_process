FROM python:3.10-alpine

WORKDIR /app
ENV PIPENV_VENV_IN_PROJECT=true
COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

COPY . /app
# override python to use venv
ENV PATH="/app/.venv/bin:${PATH}"
ENTRYPOINT [""]
