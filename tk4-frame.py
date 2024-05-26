from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()  # geometry manager

ttk.Label(frm, text="Hello World! " * 3, background="yellow", foreground="blue").grid(column=0, row=0, columnspan=5)
ttk.Spinbox(frm).grid(column=0, row=1, columnspan=5, pady=10)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2, columnspan=1)
b = ttk.Button(frm, text="Quit", command=root.destroy)
b.grid(column=3, row=2, columnspan=1)

print(b.configure().keys())

root.mainloop()