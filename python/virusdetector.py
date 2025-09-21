from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry=("200x200")

def msg():
    messagebox.showwarning("alert", "stop!VIRUS DETECTED")

btn=Button(root, text="scan for virus", command=msg)
btn.place(x=40, y=80)

root.mainloop()