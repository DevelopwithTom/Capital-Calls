FROM python:3.9.0a5-alpine3.10
MAINTAINER Tom Mac

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# RUN mkdir val_backend
WORKDIR /val_backend
RUN adduser -D user
USER user


