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
        # TODO: Manage row index in a more automatic way
        self.title = TextEntry('title', 2).var
        self.description = TextEntry('description', 3).var

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


class TextEntry:
    def __init__(self, label, row):
        self.label(label, row)
        self.var = self.field(row)

    def label(self, text, row):
        tk.Label(text=text).grid(row=row, sticky='W')

    def field(self, row):
        var = tk.StringVar()
        tk.Entry(textvariable=var).grid(row=row, column=1)

        return var
