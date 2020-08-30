from transmit.gui import TransmitGui
from transmit.io import YamlFormatter
from transmit.io import FileWriter


class TransmitController:
    def __init__(self):
        TransmitGui(self.click_transmit)

    def click_transmit(self, input):
        data = YamlFormatter().format(input)
        print(data)
        FileWriter().write(data)
