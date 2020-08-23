import tkinter as tk

FONT_FACE = 'Cantarell'


class TransmitGui:
    def __init__(self, click_transmit):
        self.click_transmit = click_transmit

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
            command=self.transmit_button_clicked
        ).grid(row=4, columnspan=2)

    def transmit_button_clicked(self):
        self.click_transmit({
            'title': self.title.get(),
            'description': self.description.get()
        })
