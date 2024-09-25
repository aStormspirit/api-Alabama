FROM python:3.12-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install -y chromium

COPY dreq.txt .
COPY scripts/test.py .

RUN pip install -r dreq.txt

RUN python3 test.py

CMD python3 test.py