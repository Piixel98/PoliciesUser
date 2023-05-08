FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
MAINTAINER Jordi Sánchez <jordisanchezmora98@gmail.com>

COPY . /home
WORKDIR /home

ENV ENV=dev
RUN pip install pipenv
RUN pipenv install --system
