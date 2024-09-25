#!/bin/bash

#создание контейнера redis для celery
docker run -p 6379:6379 -d redis

#запуск celery
celery -A tasks worker --loglevel=info --detach

#запуск uvicorn
uvicorn main:app --reload