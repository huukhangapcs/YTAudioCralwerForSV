# YTAudioCralwerForSV

Pipeline:
Read dict from file contains: speaker_name link
mkdir speaker_name -> download audio from link to that folder (using yt downloader ->mp3 format)
convert downloaded audio to wav
cut into 15s-chunks by "ffmpeg -i ... -f segment -segment_time 15 -c copy ...
choose 10 chunks that has best speaker voice quality
remove noise by https://github.com/haoxiangsnr/FullSubNet/blob/main/docs/getting_started.md
remove silence by VAD method.
========> Training audio
Caution: avoid same speaker....
