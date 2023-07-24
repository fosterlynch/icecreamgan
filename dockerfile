FROM python:3.7

RUN apt-get update && \
    apt-get install -y \
    gcc \
    g++ \ 
    ffmpeg

RUN pip install pydub mido

WORKDIR /music

COPY gan.py gan.py
COPY process_audio.py process_audio.py