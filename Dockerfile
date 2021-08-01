FROM python:3.7-alpine

COPY DYCYB/config.py /DYCYB/
COPY DYCYB/TweetStreaming.py /DYCYB/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /DYCYB
CMD ["python3", "TweetStreaming.py"]
