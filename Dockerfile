FROM python:3.12-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install -y chromium

COPY dreq.txt .
COPY scripts/Florida.py .

RUN pip install -r dreq.txt

CMD python3 Florida.py