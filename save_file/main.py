from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[("Text files", ".txt"), ("HTML file", ".html"), ("All files", ".*")],
    )
    if file is None:
        return
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()


window = Tk()
button = Button(text="Save", command=save_file)
text = Text(window)

button.pack()
text.pack()

window.mainloop()
