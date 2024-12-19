# import pytube
# import os

# yt = pytube.YouTube("https://www.youtube.com/watch?v=fTXIBFJv7eo")

# video = yt.streams.filter(only_audio=True).first()

# dest = "downloads"

# out_file = video.download(output_path=dest)

# base, ext = os.path.splitext(out_file)

# new_file = base + ".mp3"

# os.rename(out_file, new_file)

# print("Downloaded and converted to mp3 successfully!")

from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=mKky3f2cUvM"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download()