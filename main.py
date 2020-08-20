import tkinter as tk
from transmit.TransmitGui import TransmitGui
from transmit.YamlFormatter import YamlFormatter

window = tk.Tk()
window.title('TendosTransmit')

transmit = TransmitGui()
YamlFormatter()

window.mainloop()
