import tkinter as tk
from transmit.gui import TransmitGui
from transmit.io import YamlFormatter

window = tk.Tk()
window.title('TendosTransmit')

transmit = TransmitGui()
YamlFormatter()

window.mainloop()
