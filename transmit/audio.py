from pydub import AudioSegment


class AudioFile:
    def __init__(self, filename):
        sound = AudioSegment.from_mp3(filename)
        print(f"length = {sound.duration_seconds}s")
