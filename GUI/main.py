from tkinter import *
import os

# Change the working directory to the directory of the script
# os.chdir(os.path.dirname(__file__))

window = Tk()
window.geometry("420x420")
window.title("GUI")
window.config(background="#46484a")

# photo = PhotoImage(file="image.jpg")

label = Label(
    window,
    text="This is a label",
    font=("Arial", 40, "bold"),
    background="#ccc",
    fg="#51739e",
    relief=RAISED,
    bd=10,
    padx=20,
    pady=20,
    # image=photo,
    # width=100,
    # height=100,
)
# label.place(x=100, y=100)
label.pack()

window.mainloop()
