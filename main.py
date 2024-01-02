import pytube
import os

with open("youtube-video.url") as f:
    video_url = f.read()

yt = pytube.YouTube(video_url)
video = yt.streams.first()
video.player.play()

while True:
    pass  # Keep the container running indefinitely
