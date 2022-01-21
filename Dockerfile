FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN cd google-images-download && python3 setup.py install
RUN mkdir downloads
FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04
RUN apt-get update && \
    apt-get install -y ffmpeg

CMD ["python", "bot.py"]

