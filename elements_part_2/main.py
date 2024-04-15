from tkinter import *

window = Tk()

x = BooleanVar()
y = IntVar()
food = ["Pizza", "Hamburger", "Hotdog"]


def display():
    if x.get():
        print("You agree.")
    else:
        print("You don't agree")


check_button = Checkbutton(
    window,
    text="This is a checkbox",
    variable=x,
    onvalue=True,
    offvalue=False,
    command=display,
)

for index in range(len(food)):
    radio_button = Radiobutton(window, text=food[index], variable=y, value=index)
    radio_button.pack()


check_button.pack()

window.mainloop()
