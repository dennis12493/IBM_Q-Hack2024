import os
import subprocess
from pocketsphinx import AudioFile

def transcribe_video(video_file):
    wav_file = video_to_wav(video_file)
    audio_file = AudioFile(audio_file=wav_file)
    for phrase in audio_file:
        print("Transcript:", phrase)

def video_to_wav(video_file):
    wav_file = video_file.replace(".mp4", ".wav")
    if os.path.isfile(video_file):
        subprocess.call("ffmpeg -i {0} -acodec pcm_s16le -ac 1 -ar 16000 {1}".format(
            video_file, wav_file), shell=True)
        return wav_file
    else:
        raise SystemError("Video file does not exist")

# Example usage
transcribe_video("test-video.mp4")