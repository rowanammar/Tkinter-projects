from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("GPA Calculator")
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.config(bg="#181823")
title = Label(text="GPA Calculator", font=('Baskerville Old Face', 25), bg="#181823", fg="#B4CDE6")
title.pack(pady=20)
get_grade = Label(text="Enter subject's grade: ", font=('comic sans MS', 16), bg="#181823", fg="#B4CDE6")
get_grade.place(x=30, y=100)
grade = StringVar()
grade_entry = Entry(textvariable=grade, width=10, bd=3)
grade_entry.place(x=400, y=102)
get_hours = Label(text="Enter subject's no of hours: ", font=('comic sans MS', 16), bg="#181823", fg="#B4CDE6")
get_hours.place(x=30, y=160)
hours = StringVar()
hours_entry = Entry(textvariable=hours, width=10, bd=3)
hours_entry.place(x=400, y=162)
button = Button(text="Calculate", font=('comic sans MS', 16), bg="#332FD0", fg="#B4CDE6")
button.place(x=197, y=230)
result_label = Label(text="Your GPA is: ", font=('comic sans MS', 20), bg="#181823", fg="#B4CDE6")
result_label.place(x=30, y=320)
result_value = Label(text="0.0", font=('comic sans MS', 22), bg="#181823", fg="#B4CDE6")
result_value.place(x=365, y=320)
total_subjects_label = Label(text="Total no. of subjects: ", font=('comic sans MS', 20), bg="#181823", fg="#B4CDE6")
total_subjects_label.place(x=30, y=380)
total_subjects_value = Label(text="0", font=('comic sans MS', 22), bg="#181823", fg="#B4CDE6")
total_subjects_value.place(x=380, y=380)
total_hours = 0
total_points = 0
total_subjects = 0
error_label = Label(text="Enter a valid value!", font=('comic sans MS', 16), bg="#181823", fg="red")
reset_button = Button(text="Reset", font=('comic sans MS', 13), bg="#332FD0", fg="#B4CDE6")
reset_button.place(x=350, y=237)


def calculate(grades, event=None):
    global total_hours
    global total_points
    global total_subjects
    if grade.get() == "" or hours.get() == "":
        error_label.place(x=160, y=280)
        return
    if not hours.get().isnumeric():
        error_label.place(x=160, y=280)
        return
    error_label.place_forget()
    match grade.get().upper():
        case "A+":
            total_points += 4 * int(hours.get())
            total_hours += int(hours.get())
            total_subjects += 1
        case "A":
            total_points += 3.7 * int(hours.get())
            total_hours += int(hours.get())
            total_subjects += 1
        case "B+":
            total_points += 3.3 * int(hours.get())
            total_hours += int(hours.get())
            total_subjects += 1
        case "B":
            total_points += 3 * int(hours.get())
            total_hours += int(hours.get())
            total_subjects += 1
        case "C+":
            total_points += 2.7 * int(hours.get())
            total_hours += int(hours.get())
            total_subjects += 1
        case "C":
            total_points += 2.4 * int(hours.get())
            total_hours += int(hours.get())
            total_subjects += 1
        case "D+":
            total_points += 2.2 * int(hours.get())
            total_hours += int(hours.get())
            total_subjects += 1
        case "D":
            total_points += 2 * int(hours.get())
            total_hours += int(hours.get())
            total_subjects += 1
        case "F":
            total_points += 0 * int(hours.get())
            total_hours += int(hours.get())
            total_subjects += 1
        case _:
            error_label.place(x=160, y=280)
            return
    result = total_points / total_hours
    result_value.config(text=result.__format__('0.2f'))
    total_subjects_value.config(text=total_subjects)
    grade_entry.delete(0, END)
    hours_entry.delete(0, END)
    grade_entry.focus()


def show_instructions():
    instructions = """
    Grade Calculation :

A+ : 90%-100%     |   GPA: 4
A  : 85%-90%         |   GPA: 3.7
B+ : 80%-85%        |   GPA: 3.3
B  : 75%-80%         |   GPA: 3
C+ : 70%-75%       |   GPA: 2.7
C  : 65%-70%         |   GPA: 2.4
D+ : 60%-65%       |   GPA: 2.2
D  : 50%-60%        |   GPA: 2
F  : Fail                  |   GPA: 0
    """

    messagebox.showinfo("Grade Calculation ", instructions )


def focus_next(event):  # 3shan n5ly el down arrow yn2l men entry lely b3dyha
    event.widget.tk_focusNext().focus()
    return ("break")  # 3shan n-disable el default behavior bta3 el arrow


def focus_previous(event):
    event.widget.tk_focusPrev().focus()
    return ("break")


def reset():
    global total_hours
    global total_points
    global total_subjects
    total_hours = 0
    total_points = 0
    total_subjects = 0
    result_value.config(text="0.0")
    total_subjects_value.config(text="0")
    grade_entry.delete(0, END)
    hours_entry.delete(0, END)


help_button = Button(text="Help", bg='#FFFFFF', fg='#4D4C7D', command=show_instructions,
                     width=5,
                     height=1)
help_button.place(x=10, y=20)

reset_button.config(command=reset)
grade_entry.bind("<Down>", focus_next)
hours_entry.bind("<Up>", focus_previous)
button.config(command=calculate)
window.bind('<Return>', calculate)
window.mainloop()
