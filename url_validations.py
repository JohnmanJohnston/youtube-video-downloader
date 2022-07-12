import re
import requests

def possible_youtube_url(url):
    url = re.sub(r"\&t=.*.", "", url)

    if re.match(r"^(https|http)\:\/\/(youtu|www\.youtu|youtu)(\.be/.*.|be\.com/watch\?v=.*.)$", url):
        return True
    else:
        return False
        
def check_video_existence(url):
    req = requests.get(url, allow_redirects=False)
    return req.status_code == 200