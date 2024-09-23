#!/bin/bash

docker run --name my-redis -p 6379:6379 -d redis

celery -A utils worker --loglevel=info

uvicorn main:app --reload