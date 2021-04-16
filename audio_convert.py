from pydub import AudioSegment
import os
def mp3_to_wav(file):
    sound = AudioSegment.from_mp3(file)
    sound.export(file.replace("mp3","wav"), format="wav")
    os.remove(file)

def m4a_to_wav(file):
    sound = AudioSegment.from_file(file)
    sound.export(file.replace("m4a","wav"), format="wav")
    os.remove(file)