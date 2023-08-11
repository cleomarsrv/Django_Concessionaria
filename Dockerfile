FROM python:3.10.11-slim

RUN useradd -ms /bin/bash python

RUN useradd -ms /bin/bash python2

RUN pip install pipenv

RUN apt-get update && apt-get install -y nano

RUN echo 'root:python' | chpasswd

RUN echo 'python2:python' | chpasswd

RUN echo 'python:python' | chpasswd

USER python

WORKDIR /home/python/app

ENV PIPENV_VENV_IN_PROJECT=True
