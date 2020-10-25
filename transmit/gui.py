import tkinter as tk
from tkinter import filedialog
import ntpath


class TransmitGui:
    def __init__(self, click_transmit):
        self.click_transmit = click_transmit

        self.add_decorations(
            'TendosTransmit',
            'The podcast deployment tool of the future.'
        )

        self.add_mp3_button()
        self.add_text_fields()
        self.add_transmit_button()

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

    def add_mp3_button(self):
        tk.Label(text='mp3 file').grid(row=2, sticky='W')

        self.mp3_button = tk.Button(
            text='select mp3 file',
            command=self.select_mp3_file
        )
        self.mp3_button.grid(row=2, column=1)

    def select_mp3_file(self):
        # TODO: don't set None files (if they cancel)
        self.mp3_filename = filedialog.askopenfilename(
            initialdir='~', title='Select mp3 file', filetypes=[('Mp3 Files', '*.mp3')])

        filename_leaf = path_leaf(self.mp3_filename)
        self.mp3_button.config(text=filename_leaf)

    def add_text_fields(self):
        # TODO: Manage row index in a more automatic way
        title = LabeledEntry('title', 3)
        title.set_width(27)

        self.title = title.string_var
        self.summary = LabeledText('summary', 4).text
        self.episode_number = LabeledEntry('episode #', 5).string_var
        self.mp3_link = LabeledEntry('mp3 link', 6).string_var

    def add_transmit_button(self):
        tk.Button(
            text='Transmit',
            command=self.transmit_button_clicked
        ).grid(row=7, columnspan=2)

    # TODO: this should be its own InputConversion class
    def transmit_button_clicked(self):
        self.click_transmit({
            'title': self.title.get(),
            'summary': self.summary.get('1.0', 'end-1c'),
            'asset_id': f'tendos-ep{self.episode_number.get()}',
            'file_url': self.mp3_link.get(),
        })


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


class LabeledEntry:
    def __init__(self, label, row):
        self.add_label(label, row)
        self.string_var = self.add_entry(row)

    def add_label(self, text, row):
        tk.Label(text=text).grid(row=row, sticky='W')

    def add_entry(self, row):
        string_var = tk.StringVar()
        self.entry = tk.Entry(textvariable=string_var)
        self.entry.grid(row=row, column=1)

        return string_var

    def set_width(self, width):
        self.entry.config(width=width)


class LabeledText:
    def __init__(self, label, row):
        self.label(label, row)
        self.field(row)

    def label(self, text, row):
        tk.Label(text=text).grid(row=row, sticky='W')

    def field(self, row):
        self.text = tk.Text(width=30, height=5)
        self.text.grid(row=row, column=1)
