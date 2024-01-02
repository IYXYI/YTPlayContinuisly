FROM python:3.10

RUN pip install pytube

COPY main.py .

COPY youtube-video.url .

CMD ["python", "main.py"]
