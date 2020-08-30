from pydub import AudioSegment


class AudioFile:
    def __init__(self, filename):
        # TODO: from mp3
        sound = AudioSegment.from_wav(filename)
        print(f"length = {sound.duration_seconds}s")
