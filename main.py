import tkinter as tk
from transmit.controller import TransmitController
from transmit.audio import AudioFile


window = tk.Tk()
window.title('TendosTransmit')

TransmitController()
AudioFile('intro100.wav')

window.mainloop()
