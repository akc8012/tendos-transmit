import tkinter as tk

FONT_FACE = 'Cantarell'


class TransmitGui:
    def __init__(self, click_transmit):
        self.click_transmit = click_transmit

        self.add_decorations()
        self.add_text_fields()
        self.add_button()

    def add_decorations(self):
        tk.Label(
            text='TendosTransmit',
            font=(FONT_FACE, 24, 'bold')
        ).grid(row=0, columnspan=2)

        tk.Label(
            text='The podcast deployment tool of the future.',
            font=(FONT_FACE, 11, 'italic')
        ).grid(row=1, columnspan=2)

    def add_text_fields(self):
        self.field_label('title', 2)

        self.title = tk.StringVar()
        tk.Entry(
            textvariable=self.title,
        ).grid(row=2, column=1)

        self.field_label('description', 3)

        self.description = tk.StringVar()
        tk.Entry(
            textvariable=self.description,
        ).grid(row=3, column=1)

    def field_label(self, text, row):
        tk.Label(text=text).grid(row=row, sticky='W')

    def add_button(self):
        tk.Button(
            text='Transmit',
            command=self.transmit_button_clicked
        ).grid(row=4, columnspan=2)

    def transmit_button_clicked(self):
        self.click_transmit({
            'title': self.title.get(),
            'description': self.description.get()
        })
