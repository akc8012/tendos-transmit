import tkinter as tk


class TransmitGui:
    def __init__(self, click_transmit):
        self.click_transmit = click_transmit

        self.add_decorations(
            'TendosTransmit',
            'The podcast deployment tool of the future.'
        )
        self.add_text_fields()
        self.add_button()

    def add_decorations(self, header, subtitle):
        FONT_FACE = 'Cantarell'

        tk.Label(
            text=header,
            font=(FONT_FACE, 24, 'bold')
        ).grid(row=0, columnspan=2)

        tk.Label(
            text=subtitle,
            font=(FONT_FACE, 11, 'italic')
        ).grid(row=1, columnspan=2)

    def add_text_fields(self):
        # TODO: Only ONE PLACE should need to change to add a field (aka no manual dict creation)
        # TODO: Manage row index in a more automatic way
        self.title = TextEntry('title', 2).var
        self.summary = TextEntry('summary', 3).var
        self.episode_number = TextEntry('episode #', 4).var
        self.mp3_file = TextEntry('mp3 file', 5).var
        self.mp3_link = TextEntry('mp3 link', 6).var

    def add_button(self):
        tk.Button(
            text='Transmit',
            command=self.transmit_button_clicked
        ).grid(row=7, columnspan=2)

    def transmit_button_clicked(self):
        self.click_transmit({
            'title': self.title.get(),
            'summary': self.summary.get(),
            'asset_id': f'tendos-ep{self.episode_number.get()}',
            'file_url': self.mp3_link.get(),
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
