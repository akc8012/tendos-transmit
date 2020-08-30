from pydub import AudioSegment
import os


class AudioFile:
    def __init__(self, filename):
        self.file_size = os.path.getsize(filename)

        audio = AudioSegment.from_mp3(filename)
        self.duration = audio.duration_seconds
