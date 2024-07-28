from pydub import AudioSegment
from ftplib import FTP
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
