import tkinter as tk

FONT_FACE = 'Cantarell'


class TransmitGui:
    def __init__(self, click_transmit):
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

        self.description = tk.StringVar()
        tk.Entry(
            textvariable=self.description,
        ).grid(row=3, column=1)

        tk.Button(
            text='Transmit',
            command=click_transmit
        ).grid(row=4, columnspan=2)
