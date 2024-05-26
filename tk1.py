# Install: sudo apt-get install python3.11-tk
# Docs: https://docs.python.org/3/library/tkinter.html

import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello, world!")
label.pack()

root.mainloop()
