import os

from download_video import *
from convert_video_to_audio import *
from convert_audio_to_text import *
import random
from play_audio import *


def search_audio_using_text(text):

    count = 0
    for (root, dir, files) in os.walk('InputVideo/'):
        for f in files:
            count = count + 1

    number = count

    audio_list, text_list = search_audio('InputAudioChunks/AudioSplits_' + str(number), text)

    return audio_list, text_list

def play_audio_using_path(path):

    count = 0
    for (root, dir, files) in os.walk('InputVideo/'):
        for f in files:
            count = count + 1
    number = count

    play_sound_from_file('InputAudioChunks/AudioSplits_' + str(number) + '/' + path)

def url_processor(url):

    count = 0
    for (root, dir, files) in os.walk('InputVideo/'):
        for f in files:
            count = count + 1
    number = count + 1
    downloadYoutube(url, 'InputVideo/video_' + str(number))
    print("download success...")
    video_name = ''
    for (root, dir, files) in os.walk('InputVideo/video_' + str(number)):
        for f in files:
            if('.mp4' in f):
                video_name = f

    video_to_audio_converter('InputVideo/video_' + str(number) + "/" + video_name, 'InputAudio/audio_' + str(number) + '.wav')
    print("video_to_audio_converter success...")
    get_large_audio_transcription_on_silence('InputAudio/audio_' + str(number) + '.wav', 'InputAudioChunks/AudioSplits_' + str(number))
    print("get_large_audio_transcription_on_silence success...")
