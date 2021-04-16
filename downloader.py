from __future__ import unicode_literals
import youtube_dl
import os
def download_audio(audio_link, name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'dataset/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    id_list = []
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(audio_link, download=True)
        video_id = info_dict.get("id", None)
        id_list.append(video_id)
    return id_list