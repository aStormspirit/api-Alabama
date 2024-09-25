#!/bin/bash
IMAGE_NAME=$1
ENV_VARIABLE=$2
docker run --rm -v /home/vova/Desktop/WORKDIR/Alabama/data:/app/data -e DATA_ID=$ENV_VARIABLE $IMAGE_NAME
