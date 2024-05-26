# From https://docs.python.org/3/library/tkinter.html

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # https://manpages.debian.org/bookworm/tk8.6-doc/bind.3tk.en.html
        self.master.bind("<ButtonPress>", self.turn_red)
        self.pack()

    def turn_red(self, event):
        print(dir(event))
        print()
        print(dir(event.widget))
        # event.widget["activeforeground"] = "red"
        # event.widget
        event.widget.title = "test"
        event.widget.configure(background='red')

# create the application
myapp = App()

#
# here are method calls to the window manager class (since it's a master)
#
myapp.master.title("Click on me...")
myapp.master.minsize(300, 200)
myapp.master.maxsize(7000, 400)

w, h = myapp.winfo_screenwidth(), myapp.winfo_screenheight()
print(f"Screen resolution: {w} x {h}")
#myapp.overrideredirect(1)
#myapp.geometry("%dx%d+0+0" % (w, h))

myapp.master.bind("<Escape>", lambda e: e.widget.quit())

print("Click on the window...")
myapp.mainloop()