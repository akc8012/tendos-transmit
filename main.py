import tkinter as tk
from scipy.io import wavfile
from transmit.controller import TransmitController


def get_length(rate, data):
    return data.shape[0] / rate


rate, data = wavfile.read('intro100.wav')

length = get_length(rate, data)
print(f"length = {length}s")

window = tk.Tk()
window.title('TendosTransmit')

TransmitController()

window.mainloop()
