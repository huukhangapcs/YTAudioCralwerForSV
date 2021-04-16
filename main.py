from downloader import download_audio
from audio_convert import mp3_to_wav
import pandas as pd
import os
import shutil
from helper import make_dir, remove_file
import subprocess
df = pd.read_csv("link_to_download.csv")
spk_name = df["spk_name"]
link = df["link"]
# contain: spk name, link
id_list = download_audio(link)
for i in range (len(id_list)):
    make_dir(spk_name[i])
    path = spk_name[i]+"/"+id_list[i]
    shutil.move(id_list[i], path)
    command = "ffmpeg -i %s -f segment -segment_time 15 -c copy %s " % (path, spk_name[i]+"/%d.mp3")
    subprocess.run(command, shell=True)
    remove_file(path)
    
#check by hand -> then convert to wav    
    
    
    # mp3_to_wav(path)