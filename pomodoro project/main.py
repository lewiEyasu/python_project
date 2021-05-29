from tkinter import *
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = ''
timer = None

#to count down

def count_down(count):
    m, s = divmod(count, 60)
    time1 = f'{m:02d}:{s:02d}'
    canvas.itemconfig(timer_label, text=time1)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)


    else:
        start_timer()

#to start the timer

def start_timer():
    global reps
    reps += 1

    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
    elif reps % 8 == 0:
        global check_mark
        check_mark += '✔'
        label_mark.config(text=check_mark)
        window.lift()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)

        count_down(LONG_BREAK_MIN * 60)


    elif reps % 2 == 0:
        check_mark += '✔'
        label_mark.config(text=check_mark)
        window.lift()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        count_down(SHORT_BREAK_MIN * 60)


#to reset

def reset():
    global reps
    reps = 0
    global check_mark
    check_mark = ''
    canvas.itemconfig(timer_label, text='00:00')
    label_mark.config(text=check_mark)
    window.after_cancel(timer)

window = Tk()
window.title('pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)



label = Label(text='Timer', font=(FONT_NAME, 35), bg=YELLOW)
label.config(foreground=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_photo)
timer_label = canvas.create_text(100, 135, text='00:00', fill='white', font=(FONT_NAME,27, 'bold'))
canvas.grid(column=1, row=1)

label_mark = Label(text='', bg=YELLOW)
label_mark.config(foreground=GREEN,pady=15)
label_mark.grid(column=1, row=3)

button_start = Button(text='Start', command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', command=reset)
button_reset.grid(column=2, row=2)

window.mainloop()

