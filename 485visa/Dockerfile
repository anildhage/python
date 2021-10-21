FROM python:3.6.15-alpine3.13

COPY bots/config.py /bots/
COPY bots/stream.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "stream.py"]