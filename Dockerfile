FROM ubuntu:latest

RUN apt-get update && apt-get install -y mpv

COPY youtube-video.url /home/youtube-video.url

CMD ["mpv", "-loop", "0", "/home/youtube-video.url"]
