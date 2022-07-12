from pytube import YouTube
import sys
from url_validations import possible_youtube_url
from url_validations import check_video_existence

def main():
    while True:
        video_url = input("Enter the URL of the video that you want to be downloaded: ")

        if possible_youtube_url(video_url):
            if check_video_existence(video_url):
                break
            else:
                print("Sorry! The video with the URL " + "\x1b[6;30;42m" +  video_url + "\x1b[0m" + " is unavailable")
        else:
            print("Sorry! The URL " + "\x1b[6;30;42m" +  video_url + "\x1b[0m" + " is not a valid YouTube URL")

    while True:
        response = input("A video with that URL has been found. Are you sure you want to download it? (y/n) ")
        
        if response.lower() == "y":
            break
        elif response.lower() == "n":
            print("Okay, quitting this program...")
            sys.exit(0)

    print(f"Downloading the video with the URL {video_url}...")
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True).order_by("resolution").desc().first()
    stream.download()

if __name__ == "__main__":
    main()