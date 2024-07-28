import requests
from pydub import AudioSegment
import os

def load_sample(sample_path):
    return AudioSegment.from_file(sample_path)

def create_beat(kick_sample, snare_sample, hihat_sample, tempo=120, pattern="kick-snare-hihat"):
    beat_duration = int(60000 / tempo)
    beat = AudioSegment.silent(duration=0)
    
    pattern_parts = pattern.split('-')
    for part in pattern_parts:
        if part == "kick":
            beat += kick_sample[:beat_duration]
        elif part == "snare":
            beat += snare_sample[:beat_duration]
        elif part == "hihat":
            beat += hihat_sample[:beat_duration]
        beat += AudioSegment.silent(duration=beat_duration - len(beat))
    
    beat = beat * 4
    return beat

def save_beat(beat, filename="rap_beat.wav"):
    beat.export(filename, format="wav")

def upload_to_fileio(file_name):
    with open(file_name, 'rb') as f:
        files = {'file': (file_name, f)}
        response = requests.post("https://file.io", files=files)
        response.raise_for_status()
        data = response.json()
        file_url = data.get('link')
        print(f"File uploaded successfully. Download link: {file_url}")

if __name__ == "__main__":
    tempo = 140
    pattern = "kick-hihat-snare-hihat"
    kick_sample_path = "samples/kick.wav"
    snare_sample_path = "samples/snare.wav"
    hihat_sample_path = "samples/hihat.wav"

    kick_sample = load_sample(kick_sample_path)
    snare_sample = load_sample(snare_sample_path)
    hihat_sample = load_sample(hihat_sample_path)

    beat = create_beat(kick_sample, snare_sample, hihat_sample, tempo=tempo, pattern=pattern)
    file_name = "rap_beat.wav"
    save_beat(beat, file_name)

    #  File.io
    upload_to_fileio(file_name)
