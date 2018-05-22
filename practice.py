from tkinter import *
from tkinter import ttk

root = Tk()

Label(root, text="Description").grid(row=0, sticky=W, column=0)
Entry(root, width=50).grid(row=0, column=1)

Button(root, text="Submit").grid(row=0, column=8)

root.mainloop()
