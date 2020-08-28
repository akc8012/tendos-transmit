from scipy.io import wavfile


class AudioFile:
    def __init__(self, filename):
        rate, data = wavfile.read(filename)

        length = self.get_length(rate, data)
        print(f"length = {length}s")

    def get_length(self, rate, data):
        return data.shape[0] / rate
