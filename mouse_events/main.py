from tkinter import *


def do_something(event):
    print(event.x, event.y)


window = Tk()

window.bind("<Motion>", do_something)

window.mainloop()
