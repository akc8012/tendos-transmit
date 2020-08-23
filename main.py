import tkinter as tk
from transmit.gui import TransmitGui
from transmit.io import YamlFormatter
from transmit.io import FileWriter


window = tk.Tk()
window.title('TendosTransmit')


def click_transmit():
    data = YamlFormatter().format({
        'title': transmit.title.get(),
        'description': transmit.description.get()
    })

    FileWriter().write(data)


transmit = TransmitGui(click_transmit)
window.mainloop()
