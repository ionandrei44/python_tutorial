from tkinter import *


def submit():
    print("The temperature is " + str(scale.get()) + " degrees C")


window = Tk()

scale = Scale(
    window,
    from_=1000,
    to=0,
    length=600,
    orient=VERTICAL,
    font=("Consolas", 20),
    tickinterval=10,
    troughcolor="#69EAFF",
    fg="#FF1C00",
)

scale.set(
    ((scale["from"] - scale["to"]) / 2) + scale["to"]
)  # place the value in the middle of the range

scale.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()
