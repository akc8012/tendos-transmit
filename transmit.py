import tkinter as tk
window = tk.Tk()
window.title('TendosTransmit')


def click_transmit():
    print(f'hello "{title.get()}"')


FONT_FACE = 'Cantarell'

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

title = tk.StringVar()
tk.Entry(
    textvariable=title,
).pack(side='left')

tk.Label(
    text='description'
).pack(side='left')

# TODO: Use a grid to arrange these instead
description = tk.StringVar()
tk.Entry(
    textvariable=description,
).pack(side='left')

tk.Button(
    text='transmit',
    command=click_transmit
).pack(side='bottom')

window.mainloop()
