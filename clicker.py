from tkinter import *
import time
from tkinter import messagebox

window = Tk()
window.title("Clicker")
window.configure(bg='#363062')
window.minsize(height=300, width=500)
window.maxsize(height=300, width=500)
title = Label(text="Clicker", font=("Comic Sans MS", 25), bg='#363062', fg='#D8B9C3')
title.pack()
counter = 0
timer_label = Label(text="Time: 00:00", font=("Comic Sans MS", 20), bg='#363062', fg='#D8B9C3')
timer_label.place(x=30, y=150)
start_time = None  # to check if the timer is running or not

label1 = Label(text="You have clicked ", font=("Comic Sans MS", 20), bg='#363062', fg='#D8B9C3')
label1.place(x=30, y=100)

label2 = Label(text=str(counter), font=("Comic Sans MS", 20), bg='#363062', fg='#A3C7D6')
label2.place(x=260, y=100)

label3 = Label(text=" clicks.", font=("Comic Sans MS", 20), bg='#363062', fg='#D8B9C3')
label3.place(x=310, y=100)


def update_timer():
    global start_time
    if start_time is not None:  # law el timer sha8al aka dosna click
        elapsed_time = time.time() - start_time  # el time ely 3ada men wa2t el start time
        minutes, seconds = divmod(int(elapsed_time), 60)  # law  3ada 60 sec yb2a 1 min
        timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
        window.after(100, update_timer)  # 3shan el timer yb2a 3la tool we y-refresh el window kol snya


def click(event=None):
    global counter, start_time
    counter += 1
    label2.config(text=str(counter))
    if start_time is None:
        start_time = time.time()  # bn-save time awl dosa ka start time
        update_timer()  # bnst5dmha 3shan el time yfdl yt8ayar mayb2ash sabt


def reset(event=None):
    global counter, start_time
    counter = 0
    label2.config(text=str(counter))
    timer_label.config(text="Time: 00:00")
    start_time = None  # bnms7 el start time el saved dah we nbtdy men elsefr tany


def show_instructions():
    instructions = '''Welcome to  Clicker!\n\n
• Click the 'Click' button or press the spacebar to increase the click counter.\n 
• Use the 'Reset' button, Backspace, or Delete key to reset the counter.\n 
• The timer starts when you click for the first time.\n '''

    messagebox.showinfo("Instructions", instructions)


# Create the help button
help_button = Button(text="Help", font=("Comic Sans MS", 10), bg='#FFFFFF', fg='#4D4C7D', command=show_instructions,
                     width=5,
                     height=1)
help_button.place(x=10, y=20)

reset_button = Button(text="Reset", font=("Comic Sans MS", 20), bg='#4D4C7D', fg='#D8B9C3', command=reset, width=8,
                      height=1)
reset_button.place(x=300, y=200)
click_button = Button(text="Click", font=("Comic Sans MS", 20), bg='#4D4C7D', fg='#D8B9C3', command=click, width=8,
                      height=1)
click_button.place(x=70, y=200)
window.bind('<space>', click)
window.bind('<BackSpace>', reset)
window.bind('<Delete>', reset)

window.mainloop()
