#isAWW
import requests
from bs4 import BeautifulSoup
import json


def tiktok_downloader(video_url):
    output_file = 'temp/tiktok_video.mp4'
    video_id = video_url.split('?')[0].split('video/')[1]
    url=f'https://www.tikwm.com/video/media/hdplay/{video_id}.mp4'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
    return output_file

def likedin_video_downloader(video_url):
    output_file = 'temp/linkedin_video.mp4'
    content=requests.get(video_url).content
    soup=BeautifulSoup(content,'html.parser')
    meta_teag=soup.find_all("script")
    if meta_teag:
        content=meta_teag[1]
        json_data=json.loads(content.get_text())
        video_url=json_data.get('contentUrl')
        response=requests.get(video_url,stream=True)
        if response.status_code == 200:
         with open(output_file,'wb') as f:
             for chunk in response.iter_content(chunk_size=1024):
                 f.write(chunk)
         return output_file
        else:
            print("Video not found")   
    else:
     print("No META TAG")
