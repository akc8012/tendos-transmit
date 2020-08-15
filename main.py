import tkinter as tk
from Transmit import Transmit
from YamlWriter import YamlWriter

window = tk.Tk()
window.title('TendosTransmit')

transmit = Transmit()
YamlWriter()

window.mainloop()
