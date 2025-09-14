from tkinter import*
from datetime import date

root = Tk()
root.title("Getting started with widgets")
root.geometry("400x300")

lbl = Label(text="hello there!", fg = "white",bg = "#c77474", height=1, width=300 )

name_lbl = Label(text="Full Name", bg="#ee8e8e")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message 
    message = "Welcome to my Application:) \nToday's Date is:"
    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3) 

btn = Button(text="Begin", command=display, height=1, bg= "#fad8d8", fg = 'white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()