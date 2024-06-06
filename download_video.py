#!/usr/bin/env python
import os
import sys
from pytube import YouTube



def downloadYoutube(vid_url, path):
    yt = YouTube(vid_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)

    yt.download(path)


# video url
#url = 'https://www.youtube.com/watch?v=WsEQjeZoEng&ab_channel=Google'
# path to where you want to save the video
#path = 'video/pichai.wav'
#downloadYoutube(url, path)
