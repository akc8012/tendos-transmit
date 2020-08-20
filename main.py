import tkinter as tk
from transmit.TransmitGui import TransmitGui
from transmit.YamlWriter import YamlWriter

window = tk.Tk()
window.title('TendosTransmit')

transmit = TransmitGui()
YamlWriter()

window.mainloop()
