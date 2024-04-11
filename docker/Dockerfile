FROM python:3.12-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc curl \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app 
COPY pyproject.toml /app
WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG False
ENV BASE_DIR "app/"

EXPOSE 80/tcp

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . /app

CMD python -m uvicorn app.main:app --host 0.0.0.0 --port 80