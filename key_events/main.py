from tkinter import *


def do_something(event):
    label.config(text=event.keysym)


window = Tk()
window.geometry("300x100")

window.bind("<Key>", do_something)

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()
