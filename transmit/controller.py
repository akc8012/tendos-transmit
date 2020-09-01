import datetime

from transmit.gui import TransmitGui
from transmit.io import YamlFormatter
from transmit.io import FileWriter
from transmit.audio import AudioFile


class TransmitController:
    def __init__(self):
        self.gui = TransmitGui(self.click_transmit)

    def click_transmit(self, input):
        if hasattr(self.gui, 'mp3_filename'):
            audio = AudioFile(self.gui.mp3_filename)
            # BUG: this should be in minutes, not seconds
            # TODO: this should be in InputConversion class!!
            input['duration'] = audio.duration
            input['length'] = audio.file_size
            input['date'] = datetime.date.today()

        data = YamlFormatter().format(input)
        print(data)

        FileWriter().write(data)
