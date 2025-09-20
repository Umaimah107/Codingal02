from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator")
root.geometry("400x250")

lbl = Label(root, text="Enter your Birth Year", fg="white", bg="#c77474", height=1, width=300)

birth_lbl = Label(root, text="Birth Year", bg="#ee8e8e")
birth_entry = Entry(root)

text_box = Text(root, height=2, width=40)

def calculate_age():
    """Take birth year, calculate age, and display result."""
    try:
        birth_year = int(birth_entry.get())
        current_year = date.today().year 
        if birth_year > current_year:
            text_box.delete(1.0, END)
            text_box.insert(END, "Birth year cannot be in the future!")
        else:
            age = current_year - birth_year
            text_box.delete(1.0, END)
            text_box.insert(END, f"You are {age} years old in {current_year}.")
    except ValueError:
        text_box.delete(1.0, END)
        text_box.insert(END, "Please enter a valid year!")

def clear_text():
    """Clear all fields and text box."""
    birth_entry.delete(0, END)
    text_box.delete(1.0, END)

btn_frame = Frame(root, bg="#fff2f2")
btn = Button(btn_frame, text="Calculate", command=calculate_age, height=1, bg="#fad8d8", fg='black')
clear_btn = Button(btn_frame, text="Clear", command=clear_text, height=1, bg="#ffb3b3", fg='black')

lbl.pack()
birth_lbl.pack()
birth_entry.pack()
btn_frame.pack()
btn.grid(row=0, column=0)
clear_btn.grid(row=0, column=1)
text_box.pack()

root.mainloop()