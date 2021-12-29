FROM python:3.9

WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y install python3-dev

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ /app

WORKDIR /app