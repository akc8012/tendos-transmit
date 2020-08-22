import tkinter as tk
# TODO: pylint: disable=import-error
from transmit.io import YamlFormatter

FONT_FACE = 'Cantarell'


class TransmitGui:
    def __init__(self):
        tk.Label(
            text='TendosTransmit',
            font=(FONT_FACE, 24, 'bold')
        ).grid(row=0, columnspan=2)

        tk.Label(
            text='The podcast deployment tool of the future.',
            font=(FONT_FACE, 11, 'italic')
        ).grid(row=1, columnspan=2)

        tk.Label(
            text='title'
        ).grid(row=2, sticky='W')

        self.title = tk.StringVar()
        tk.Entry(
            textvariable=self.title,
        ).grid(row=2, column=1)

        tk.Label(
            text='description'
        ).grid(row=3, sticky='W')

        # TODO: Use a grid to arrange these instead
        self.description = tk.StringVar()
        tk.Entry(
            textvariable=self.description,
        ).grid(row=3, column=1)

        tk.Button(
            text='Transmit',
            command=self.click_transmit
        ).grid(row=4, columnspan=2)

    def click_transmit(self):
        output = YamlFormatter().format(
            {'title': self.title.get(), 'description': self.description.get()})
        print(output)
