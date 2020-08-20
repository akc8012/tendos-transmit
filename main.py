import tkinter as tk
from Transmit import TransmitGui
from YamlWriter import YamlWriter

window = tk.Tk()
window.title('TendosTransmit')

transmit = TransmitGui()
YamlWriter()

window.mainloop()
