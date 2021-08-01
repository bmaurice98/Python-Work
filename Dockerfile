FROM python:3

COPY DYCYB/config.py /DYCYB/
COPY DYCYB/TweetStreaming.py /DYCYB/
COPY requirements.txt /tmp
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /DYCYB
CMD ["python3", "TweetStreaming.py"]
