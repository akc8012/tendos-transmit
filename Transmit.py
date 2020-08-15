import tkinter as tk

FONT_FACE = 'Cantarell'


class Transmit:
    def __init__(self):
        tk.Label(
            text='TendosTransmit',
            font=(FONT_FACE, 24, 'bold')
        ).pack()

        tk.Label(
            text='The podcast deployment tool of the future.',
            font=(FONT_FACE, 11, 'italic')
        ).pack()

        tk.Label(
            text='title'
        ).pack(side='left')

        self.title = tk.StringVar()
        tk.Entry(
            textvariable=self.title,
        ).pack(side='left')

        tk.Label(
            text='description'
        ).pack(side='left')

        # TODO: Use a grid to arrange these instead
        self.description = tk.StringVar()
        tk.Entry(
            textvariable=self.description,
        ).pack(side='left')

        tk.Button(
            text='transmit',
            command=self.click_transmit
        ).pack(side='bottom')

    def click_transmit(self):
        print(
            f'title "{self.title.get()}", description: "{self.description.get()}"'
        )
