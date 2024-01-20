import time
from tkinter import *
from plyer import notification

window = Tk()
window.title("Countdown Timer")
window.configure(bg='#500734')
window.minsize(width=500, height=500)
window.maxsize(width=600, height=600)
title = Label(window, text="Countdown Clock", font=("Imprint MT shadow", 25), bg='#500734', fg='#ffd6ee')
title.pack(pady=10)
label1 = Label(text="Current time : ", font=("Comic Sans MS", 20), bg='#500734', fg='#ffd6ee')
label1.pack(pady=10)
# to print current time
time_now = Label(window, font=("Comic Sans MS", 20), bg='#500734', fg='white')
button1 = Button(window, text='start', height=2, width=10, bd=3, font=("Comic Sans MS", 10), bg='#e27daf', fg='#500734')


def update_time():  # bnst5dmha 3shan el time yfdl yt8ayar mayb2ash sabt
    current_time = time.strftime('%I:%M:%S %p')
    time_now.config(text=current_time)
    time_now.after(1000, update_time)  # mdynha parameters en kol 1000 ms aka 1 sec elwa2t yt8ayar by recursion


time_now.pack()
update_time()

hours = IntVar()
minutes = IntVar()
seconds = IntVar()
label2 = Label(window, text="Enter time :", font=("Comic Sans MS", 15), bg='#500734', fg='#ffd6ee')
label2.place(x=10, y=190)
hours_entry = Entry(window, textvariable=hours, width=10, bd=5)
hours_entry.place(x=130, y=195)
minutes_entry = Entry(window, textvariable=minutes, width=10, bd=5)
minutes_entry.place(x=220, y=195)
second_entry = Entry(window, textvariable=seconds, width=10, bd=5)
second_entry.place(x=310, y=195)
remaining_time_label = Label(window, font=("Comic Sans MS", 20), bg='#500734', fg='white')
remaining_time_label.place(x=175, y=300)
time_over = Label(window, font=("Comic Sans MS", 20), bg='#500734', fg='red')
time_over.place(x=170, y=300)


def pink():
    window.configure(bg='#500734')
    title.configure(bg='#500734', fg='#ffd6ee')
    label1.configure(bg='#500734', fg='#ffd6ee')
    time_now.configure(bg='#500734', fg='white')
    label2.configure(bg='#500734', fg='#ffd6ee')
    remaining_time_label.configure(bg='#500734', fg='white')
    time_over.configure(bg='#500734', fg='red')
    button1.configure(bg='#e27daf', fg='#500734')


def blue():
    window.configure(bg='#0f1949')
    title.configure(bg='#0f1949', fg='#94b4da')
    label1.configure(bg='#0f1949', fg='#94b4da')
    time_now.configure(bg='#0f1949', fg='white')
    label2.configure(bg='#0f1949', fg='#94b4da')
    remaining_time_label.configure(bg='#0f1949', fg='white')
    time_over.configure(bg='#0f1949', fg='red')
    button1.configure(bg='#427fa5', fg='#1a1a2e')


def dark():
    window.configure(bg='#383838')
    title.configure(bg='#383838', fg='#FFB6C1')
    label1.configure(bg='#383838', fg='#FFB6C1')
    time_now.configure(bg='#383838', fg='white')
    label2.configure(bg='#383838', fg='#FFB6C1')
    remaining_time_label.configure(bg='#383838', fg='white')
    time_over.configure(bg='#383838', fg='red')
    button1.configure(bg='#D3D3D3', fg='#B91354')


def light():
    window.configure(bg='#f5f5f5')
    title.configure(bg='#f5f5f5', fg='#500734')
    label1.configure(bg='#f5f5f5', fg='#500734')
    time_now.configure(bg='#f5f5f5', fg='black')
    label2.configure(bg='#f5f5f5', fg='#500734')
    remaining_time_label.configure(bg='#f5f5f5', fg='black')
    time_over.configure(bg='#f5f5f5', fg='red')
    button1.configure(bg='#e27daf', fg='#500734')


list = Menubutton(window, text="Themes", font=("Comic Sans MS", 10))
list.menu = Menu(list, tearoff=0)
list["menu"] = list.menu
list.menu.add_command(label="Pink", command=pink)
list.menu.add_command(label="Blue", command=blue)
list.menu.add_command(label="Dark", command=dark)
list.menu.add_command(label="Light", command=light)
list.place(x=410, y=25)


# 3yza rl function dy ta5od el user  input we t7wlo kolo ly seconds
# b3d keda tbd2 t2ll el seconds one by one l7d ma nwsl zero
# awl ma ywsl zero yb3t notification we yren
def countdown():
    total_seconds = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    while total_seconds > 0:
        minute, second = divmod(total_seconds, 60)  # 3shan lw el seconds > 60 yb2a el minutes = el seconds / 60
        hour = 0
        if minute > 60:
            hour, minute = divmod(minute, 60)  # 3shan lw el minutes > 60 yb2a el hour = el minutes / 60
        time_remaining = "{:02d} : {:02d} : {:02d}".format(hour, minute, second)
        remaining_time_label.config(text=time_remaining)
        window.update()  # 3shan el window t8yr kol sanya
        time.sleep(1)  # 3shan el intervals tb2a tb2a sanya
        total_seconds -= 1
    if total_seconds <= 0:
        notification.notify(
            title="Time's up!",
            message='Time has ended',
            app_name='Countdown Timer',
            app_icon='clipart6385.ico',
            timeout=5
        )
        remaining_time_label.config(text="")
        time_over.config(text="Time's up!!")


def button_click(event=None):
    time_over.config(text="")
    countdown()


button1.config(command=button_click)
button1.place(x=200, y=250)
window.bind('<Return>', button_click)
window.mainloop()
