from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(count)


def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def back():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()
window.geometry("420x420")
window.title("GUI")
window.config(background="#46484a")


button = Button(
    window,
    text="Click me",
    command=click,
    font=("Comic Sans", 30),
    fg="#51739e",
)
submit_button = Button(
    window,
    text="Submit",
    command=submit,
    font=("Comic Sans", 30),
    fg="#51739e",
)
delete_button = Button(
    window,
    text="Delete",
    command=delete,
    font=("Comic Sans", 30),
    fg="#51739e",
)
back_button = Button(
    window,
    text="Back",
    command=back,
    font=("Comic Sans", 30),
    fg="#51739e",
)
entry = Entry(font=("Arial", 50), show="*")

button.pack()
submit_button.pack()

entry.insert(0, "Andrei")
entry.pack()

delete_button.pack()
back_button.pack()


window.mainloop()
