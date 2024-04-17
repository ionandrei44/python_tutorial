from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab_1 = Frame(notebook)
tab_2 = Frame(notebook)

notebook.add(tab_1, text="Tab 1")
notebook.add(tab_2, text="Tab 2")
notebook.pack(expand=True, fill="both")

Label(tab_1, text="This is tab 1", width=50, height=25).pack()
Label(tab_2, text="This is tab 2", width=50, height=25).pack()


window.mainloop()
