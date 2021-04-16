from __future__ import unicode_literals
import youtube_dl
import os
def download_audio(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    id_list = []
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for audio_link in link:
            info_dict = ydl.extract_info(audio_link, download=True)
            id = info_dict.get("id", None)
            id_list.append('%s.%s'% (id, "mp3"))
    return id_list