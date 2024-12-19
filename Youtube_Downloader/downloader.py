from pytube import YouTube
import re

def is_valid_youtube_url(url):
    # Simple regex to check if the URL is a valid YouTube video URL
    youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+')
    return youtube_regex.match(url)

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    if not is_valid_youtube_url(url):
        raise ValueError("Invalid YouTube URL")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Download the video to the specified directory
    yd.download("/Users/alexeirusu/Desktop/Python_Automations/image_editer/Youtube_Downloader/downloads")
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))