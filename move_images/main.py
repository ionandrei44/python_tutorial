from tkinter import *


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)


def move_left(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())


def move_right(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())


window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

label = Label(window, bg="green", width=10)
label.place(x=10, y=50)

window.mainloop()
