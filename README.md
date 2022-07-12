# youtube-video-downloader
A Python program downloads a YouTube video with a URL that is inputted by the user

This application used to download YouTube videos uses [PyTube](https://github.com/pytube/pytube) to download the videos.

The application first asks the user, for the URL of the video using the `input()` function, and stores it in a variable `video_url`.
```
 video_url = input("Enter the URL of the video that you want to be downloaded: ")
```
Then, it checks if the URL entered is a valid YouTube URL, using the power of regular expressions. It is done in `url_validations.py` in a function `possible_youtube_url()`
```
def possible_youtube_url(url):
    url = re.sub(r"\&t=.*.", "", url)

    if re.match(r"^(https|http)\:\/\/(youtu|www\.youtu|youtu)(\.be/.*.|be\.com/watch\?v=.*.)$", url):
        return True
    else:
        return False
```

So then, we know that the URL that the user has entered, is a URL that belongs to YouTube. Now, we have to make sure that the video actually exists. This is done in `check_video_existence()`

```
def check_video_existence(url):
    req = requests.get(url, allow_redirects=False)
    return req.status_code == 200
```

If the video with the URL exists, it then uses [PyTube](https://github.com/pytube/pytube) to download the video
```
print(f"Downloading the video with the URL {video_url}...")
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True).order_by("resolution").desc().first()
    stream.download()
```
