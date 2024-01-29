import time
from tkinter import *
from plyer import notification

window = Tk()
window.title("Promodoro")
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.config(bg="#680747")
title = Label(window, text="Promodoro", font=("Castellar", 25), bg='#680747', fg='#F1BBD5')
title.pack()
label1 = Label(window, text="Time now", font=("Comic Sans MS", 20), bg='#680747', fg='#F1BBD5')
label1.pack()
time_now = Label(window, font=("Comic Sans MS", 20), bg='#680747', fg='white')
label2 = Label(window, text="How many sessions ?", font=("Comic Sans MS", 16), bg='#680747', fg='#F1BBD5')
label2.place(x=10, y=170)
sessions = IntVar()
sessions_entry = Entry(window, textvariable=sessions, width=10, bd=5)
sessions_entry.place(x=400, y=172)
label3 = Label(window, text="Enter study time in minutes :", font=("Comic Sans MS", 16), bg='#680747', fg='#F1BBD5')
label3.place(x=10, y=220)
study_time = IntVar()
study_time_entry = Entry(window, textvariable=study_time, width=10, bd=5)
study_time_entry.place(x=400, y=222)
label5 = Label(window, text="Enter break time in minutes :", font=("Comic Sans MS", 16), bg='#680747', fg='#F1BBD5')
label5.place(x=10, y=270)
break_time = IntVar()
break_time_entry = Entry(window, textvariable=break_time, width=10, bd=5)
break_time_entry.place(x=400, y=272)
label4 = Label(window, text="Remaining Time : ", font=("Comic Sans MS", 20), bg='#680747', fg='#F1BBD5')
label4.place(x=10, y=320)
remaining_time_label = Label(window, font=("Comic Sans MS", 30), bg='#680747', fg='#F1BBD5')
remaining_time_label.place(x=140, y=370)
button = Button(window, text="Start", font=("Comic Sans MS", 14), bg='#F1BBD5', fg='#680747')
themes = ['pink', 'purple', 'blue', 'green', 'brown', 'dark', 'pastel']


def pink():
    window.config(bg="#680747")
    title.config(bg="#680747", fg="#F1BBD5")
    label1.config(bg="#680747", fg="#F1BBD5")
    label2.config(bg="#680747", fg="#F1BBD5")
    label3.config(bg="#680747", fg="#F1BBD5")
    label4.config(bg="#680747", fg="#F1BBD5")
    label5.config(bg="#680747", fg="#F1BBD5")
    remaining_time_label.config(bg="#680747")
    button.config(bg="#F1BBD5", fg="#680747")
    time_now.config(bg="#680747")


def purple():
    window.configure(bg='#371B58')
    title.config(bg='#371B58', fg='#C4BBF0')
    label1.config(bg='#371B58', fg='#C4BBF0')
    label2.config(bg='#371B58', fg='#C4BBF0')
    label3.config(bg='#371B58', fg='#C4BBF0')
    label4.config(bg='#371B58', fg='#C4BBF0')
    label5.config(bg='#371B58', fg='#C4BBF0')
    remaining_time_label.config(bg='#371B58')
    button.config(bg='#C4BBF0', fg='#371B58')
    time_now.config(bg='#371B58')


def blue():
    window.configure(bg='#0B2447')
    title.config(bg='#0B2447', fg='#A5D7E8')
    label1.config(bg='#0B2447', fg='#A5D7E8')
    label2.config(bg='#0B2447', fg='#A5D7E8')
    label3.config(bg='#0B2447', fg='#A5D7E8')
    label4.config(bg='#0B2447', fg='#A5D7E8')
    label5.config(bg='#0B2447', fg='#A5D7E8')
    remaining_time_label.config(bg='#0B2447')
    button.config(bg='#A5D7E8', fg='#0B2447')
    time_now.config(bg='#0B2447')


def green():
    window.configure(bg='#698269')
    title.config(bg='#698269', fg='#E1EEDD')
    label1.config(bg='#698269', fg='#E1EEDD')
    label2.config(bg='#698269', fg='#E1EEDD')
    label3.config(bg='#698269', fg='#E1EEDD')
    label4.config(bg='#698269', fg='#E1EEDD')
    label5.config(bg='#698269', fg='#E1EEDD')
    remaining_time_label.config(bg='#698269')
    button.config(bg='#E1EEDD', fg='#698269')
    time_now.config(bg='#698269')


def brown():
    window.configure(bg='#553939')
    title.config(bg='#553939', fg='#D7C0AE')
    label1.config(bg='#553939', fg='#D7C0AE')
    label2.config(bg='#553939', fg='#D7C0AE')
    label3.config(bg='#553939', fg='#D7C0AE')
    label4.config(bg='#553939', fg='#D7C0AE')
    label5.config(bg='#553939', fg='#D7C0AE')
    remaining_time_label.config(bg='#553939')
    button.config(bg='#D7C0AE', fg='#553939')
    time_now.config(bg='#553939')


def dark():
    window.configure(bg='#454545')
    title.config(bg='#454545', fg='#FB2576')
    label1.config(bg='#454545', fg='#FB2576')
    label2.config(bg='#454545', fg='#FB2576')
    label3.config(bg='#454545', fg='#FB2576')
    label4.config(bg='#454545', fg='#FB2576')
    label5.config(bg='#454545', fg='#FB2576')
    remaining_time_label.config(bg='#454545')
    button.config(bg='#A12559', fg='#F4ABC4')
    time_now.config(bg='#454545')


def pastel():
    window.configure(bg='#FF9B9B')
    title.config(bg='#FF9B9B', fg='#E3F4F4')
    label1.config(bg='#FF9B9B', fg='#E3F4F4')
    label2.config(bg='#FF9B9B', fg='#E3F4F4')
    label3.config(bg='#FF9B9B', fg='#E3F4F4')
    label4.config(bg='#FF9B9B', fg='#E3F4F4')
    label5.config(bg='#FF9B9B', fg='#E3F4F4')
    remaining_time_label.config(bg='#FF9B9B')
    button.config(bg='#B7D3DF', fg='#F9F9F9')
    time_now.config(bg='#FF9B9B')


list = Menubutton(window, text="Themes", font=("Comic Sans MS", 10))
list.menu = Menu(list, tearoff=0)
list["menu"] = list.menu
list.place(x=410, y=30)

list.menu.add_command(label="pink", command=pink)
list.menu.add_command(label="purple", command=purple)
list.menu.add_command(label='blue', command=blue)
list.menu.add_command(label='green', command=green)
list.menu.add_command(label='brown', command=brown)
list.menu.add_command(label='dark', command=dark)
list.menu.add_command(label='pastel', command=pastel)


def study():
    label4.config(text="Remaining study Time : ")
    total_study_time = study_time.get() * 60
    while total_study_time > 0:
        minute, second = divmod(total_study_time, 60)
        hour = 0
        if minute > 60:
            hour, minute = divmod(minute, 60)  # 3shan lw el minutes > 60 yb2a el hour = el minutes / 60
        time_remaining = "{:02d} : {:02d} : {:02d}".format(hour, minute, second)
        remaining_time_label.config(text=time_remaining, fg='white')
        window.update()  # 3shan el window t8yr kol sanya
        time.sleep(1)  # 3shan el intervals tb2a tb2a sanya
        total_study_time -= 1

    if total_study_time <= 0:
        remaining_time_label.config(text="00 : 00 : 00", fg='red')
        notification.notify(
            title="study time is over",
            message='take a break',
            app_name='promodoro',
            app_icon='alarmicon.ico',
            timeout=5
        )


def break_timer():
    label4.config(text="Remaining break Time : ")
    total_break_time = break_time.get() * 60
    while total_break_time > 0:
        minute, second = divmod(total_break_time, 60)
        hour = 0
        if minute > 60:
            hour, minute = divmod(minute, 60)  # 3shan lw el minutes > 60 yb2a el hour = el minutes / 60
        time_remaining = "{:02d} : {:02d} : {:02d}".format(hour, minute, second)
        remaining_time_label.config(text=time_remaining, fg='white')
        window.update()  # 3shan el window t8yr kol sanya
        time.sleep(1)  # 3shan el intervals tb2a tb2a sanya
        total_break_time -= 1
        if total_break_time <= 0:
            remaining_time_label.config(text="00 : 00 : 00", fg='red')
            notification.notify(
                title="break time is over",
                message='start studying',
                app_name='promodoro',
                app_icon='alarmicon.ico',
                timeout=5
            )


def start(event=None):
    for i in range(sessions.get()):
        study()
        break_timer()


button.config(command=start)
button.place(x=227, y=450)
window.bind('<Return>', start)


def update_time():
    current_time = time.strftime('%I:%M:%S %p')
    time_now.config(text=current_time)
    time_now.after(1000, update_time)


time_now.pack()
update_time()
window.mainloop()
