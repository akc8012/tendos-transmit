import tkinter as tk
window = tk.Tk()


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

title = tk.StringVar()
tk.Entry(
    textvariable=title
).pack()

tk.Button(
    text='transmit',
    command=click_transmit
).pack()

window.mainloop()
