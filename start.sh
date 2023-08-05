#!/bin/bash

pipenv shell

pipenv install

source .venv/bin/activate

python3 manage.py runserver 0.0.0.0:8000

tail -f /dev/null
