FROM python:3.10.11-slim

RUN useradd -ms /bin/bash python

RUN pip install pipenv

USER root

RUN apt-get update && apt-get install -y nano

RUN echo 'root:python' | chpasswd

WORKDIR /home/python/app

ENV PIPENV_VENV_IN_PROJECT=True
