import random
from tkinter import *

window = Tk()
window.title("Password Generator")
window.minsize(500, 400)
window.maxsize(2000, 400)
window.config(bg='#5C527F')
title = Label(text="Password Generator", font=("Comic Sans MS", 23), bg='#5C527F', fg="#261C2C")
title.pack(pady=10)
lower_chars = "abcdefghijklmnopqrstuvwxyz12334567890!@#$%^&*()?"
upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12334567890!@#$%^&*()?"
label1 = Label(text="Password Length :", font=("Comic Sans MS", 17), bg='#5C527F', fg="#261C2C")
label1.place(x=20, y=80)
password_length = IntVar()
repetition_var = IntVar()
use_upper_var = IntVar()
pass_length = Entry(textvariable=password_length, font=("Comic Sans MS", 17), width=5, bd=5)
pass_length.place(x=250, y=80)
repetition = Checkbutton(text="Allow repetition", font=("Comic Sans MS", 15), bg='#5C527F', fg="#261C2C",
                         activebackground='#5C527F',
                         variable=repetition_var)
repetition.place(x=20, y=120)
use_upper = Checkbutton(text="Use Upper Case", font=("Comic Sans MS", 15), fg="#261C2C", bg='#5C527F',
                        activebackground='#5C527F',
                        variable=use_upper_var)
use_upper.place(x=20, y=160)
generated_password = Label(text=" ", font=("PMingLitJ-ExtB", 28), bg='#5C527F', fg="white")


# random.sample by5tar mn8er tekrar
# random.choice by5tar by tkrar 3ady
def generate():
    if repetition_var.get() and use_upper_var.get():
        password = "".join(random.choices(upper_chars, k=password_length.get()))
        generated_password.config(text=password)

    elif repetition_var.get() and not use_upper_var.get():
        password = "".join(random.choices(lower_chars, k=password_length.get()))
        generated_password.config(text=password)

    elif not repetition_var.get() and use_upper_var.get():
        password = "".join(random.sample(upper_chars, k=password_length.get()))
        generated_password.config(text=password)

    elif not repetition_var.get() and not use_upper_var.get():
        password = "".join(random.sample(lower_chars, k=password_length.get()))
        generated_password.config(text=password)


generated_password.place(relx=0.5, rely=0.7, anchor=CENTER)


def copy(event=None):
    window.clipboard_clear()
    window.clipboard_append(generated_password.cget("text"))


def click(event=None):
    generate()


button_frame = Frame(window, bg="#5C527F")  # bn3ml frame 3shan n7dd feha el buttons
button_frame.pack(side="bottom", pady=20)
generate_pass = Button(button_frame, text="Generate", font=("Comic Sans MS", 15), bg='#3E2C41', fg='white', width=10,
                       height=1, command=click)
generate_pass.pack(side="left", padx=5)
copy_button = Button(button_frame, text="Copy", font=("Comic Sans MS", 15), bg='#3E2C41', fg='white', width=10,
                     height=1, command=copy)
copy_button.pack(side="right", padx=5)
window.bind('<Return>', click)
window.bind('<Control-c>', copy)
window.mainloop()
