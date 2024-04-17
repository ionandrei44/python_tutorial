from tkinter import *

window = Tk()

first_name_label = Label(window, text="First name").grid(row=0, column=0)
first_name_entry = Entry(window).grid(row=0, column=1)

last_name_label = Label(window, text="Last name").grid(row=1, column=0)
last_name_entry = Entry(window).grid(row=1, column=1)

email_label = Label(window, text="Email").grid(row=2, column=0)
email_entry = Entry(window).grid(row=2, column=1)

button = Button(window, text="Submit").grid(row=3, column=0, columnspan=2)


window.mainloop()
