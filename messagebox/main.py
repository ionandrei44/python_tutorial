from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(
    #     title="This is an info message box", message="This is a message"
    # )
    # messagebox.showwarning(
    #     title="This is an info message box", message="This is a message"
    # )
    # messagebox.showerror(title="ERROR", message="Something went wrong")
    if messagebox.askokcancel(title="Ask ok  cancel", message="Cancel?"):
        print("Not canceled")
    else:
        print("Canceled")


window = Tk()

button = Button(window, command=click, text="Click me")
button.pack()

window.mainloop()
