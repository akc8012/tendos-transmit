import tkinter as tk
window = tk.Tk()


def click_button():
    print('you have touched me')


font_face = 'Cantarell'

tk.Label(
    text='TendosTransmit',
    font=(font_face, 24, 'bold')
).pack()

tk.Label(
    text='The podcast deployment tool of the future.',
    font=(font_face, 11, 'italic')
).pack()

tk.Button(
    text='touch me',
    command=click_button
).pack()

window.mainloop()
