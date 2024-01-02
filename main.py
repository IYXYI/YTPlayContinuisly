import pytube
import os

video_url = os.environ["YOUTUBE_VIDEO_URL"]
yt = pytube.YouTube(video_url)
video = yt.streams.first()
video.player.play()

while True:
    pass  # Keep the container running indefinitely
