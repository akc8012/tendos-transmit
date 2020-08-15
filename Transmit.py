import tkinter as tk

FONT_FACE = 'Cantarell'


class Transmit:
    def __init__(self):
        tk.Label(
            text='TendosTransmit',
            font=(FONT_FACE, 24, 'bold')
        ).grid(row=0)

        tk.Label(
            text='The podcast deployment tool of the future.',
            font=(FONT_FACE, 11, 'italic')
        ).grid(row=1)

        tk.Label(
            text='title'
        ).grid(row=2)

        self.title = tk.StringVar()
        tk.Entry(
            textvariable=self.title,
        ).grid(row=2, column=1)

        tk.Label(
            text='description'
        ).grid(row=3)

        # TODO: Use a grid to arrange these instead
        self.description = tk.StringVar()
        tk.Entry(
            textvariable=self.description,
        ).grid(row=3, column=1)

        tk.Button(
            text='transmit',
            command=self.click_transmit
        ).grid(row=4)

    def click_transmit(self):
        print(
            f'title "{self.title.get()}", description: "{self.description.get()}"'
        )
