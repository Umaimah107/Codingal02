from tkinter import *

root = Tk()
root.title("Number Multiplier")
root.geometry("400x250")


lbl = Label(root, text="Enter two numbers to multiply", fg="white", bg="#c77474", height=1, width=300)

num1_lbl = Label(root, text="First Number", bg="#ee8e8e")
num1_entry = Entry(root)

num2_lbl = Label(root, text="Second Number", bg="#ee8e8e")
num2_entry = Entry(root)

text_box = Text(root, height=2, width=40)

def multiply_numbers():
    """Take numbers from entry fields, multiply them, and display the result."""
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 * num2
        text_box.delete(1.0, END)
        text_box.insert(END, f"The product of {num1} × {num2} = {result}")
    except ValueError:
        text_box.delete(1.0, END)
        text_box.insert(END, "Please enter valid numbers!")

def clear_text():
    """Clear all fields and text box."""
    num1_entry.delete(0, END)
    num2_entry.delete(0, END)
    text_box.delete(1.0, END)

btn_frame = Frame(root, bg="#fff2f2")
btn = Button(btn_frame, text="Multiply", command=multiply_numbers, height=1, bg="#fad8d8", fg='black')
clear_btn = Button(btn_frame, text="Clear", command=clear_text, height=1, bg="#ffb3b3", fg='black')

lbl.pack()
num1_lbl.pack()
num1_entry.pack()
num2_lbl.pack()
num2_entry.pack()
btn_frame.pack()
btn.grid(row=0, column=0)
clear_btn.grid(row=0, column=1)
text_box.pack()

root.mainloop()
