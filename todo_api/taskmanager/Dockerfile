FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /todo_api

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod -R 777 ./
