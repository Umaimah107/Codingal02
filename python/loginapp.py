from tkinter import *
from datetime import date 

root = Tk()
root.title("Login App")
root.geometry("400x250")

lbl = Label(root, text="Enter your Login Details", fg="white", bg="#c77474", height=1, width=300)

username_lbl = Label(root, text="Username", bg="#ee8e8e")
username_entry = Entry(root)

password_lbl = Label(root, text="Password", bg="#ee8e8e")
password_entry = Entry(root, show="*")

text_box = Text(root, height=2, width=40)

def check_login():
    """Check username and password, display success or error."""
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        text_box.delete(1.0, END)
        text_box.insert(END, "Login Successful! Welcome Admin.")
    else:
        text_box.delete(1.0, END)
        text_box.insert(END, "Invalid Username or Password!")

def clear_text():
    """Clear all fields and text box."""
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    text_box.delete(1.0, END)

btn_frame = Frame(root, bg="#fff2f2")
btn = Button(btn_frame, text="Login", command=check_login, height=1, bg="#fad8d8", fg='black')
clear_btn = Button(btn_frame, text="Clear", command=clear_text, height=1, bg="#ffb3b3", fg='black')

lbl.pack()
username_lbl.pack()
username_entry.pack()
password_lbl.pack()
password_entry.pack()
btn_frame.pack()
btn.grid(row=0, column=0)
clear_btn.grid(row=0, column=1)
text_box.pack()

root.mainloop()
