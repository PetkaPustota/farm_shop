FROM python:3.12-alpine

COPY requirements.txt /temp/requirements.txt
COPY . /codes
WORKDIR /codes
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password code-user