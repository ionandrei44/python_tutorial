from tkinter import *
from tkinter.ttk import *


def start(progress=0):

    if progress < 100:
        progress += 1
        bar["value"] = progress
        percent.set(str(progress) + "%")
        text.set(str(int(progress / 10)) + "/10" + " tasks completed")
        window.after(50, start, progress)


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()
