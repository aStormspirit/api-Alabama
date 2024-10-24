#!/bin/bash

#создание контейнера redis для celery
docker run --name my-redis -p 6379:6379 -d redis

#создание контейнера со скриптами
docker build -t <name> .


#запуск celery
celery -A utils worker --loglevel=info

#запуск uvicorn
uvicorn main:app --reload