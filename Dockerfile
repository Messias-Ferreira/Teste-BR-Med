FROM python:3

ENV PYTHONPATH=$PWD

WORKDIR /app

COPY  . .

RUN pip install -q --upgrade pip

RUN pip install -r ./requirements.txt

