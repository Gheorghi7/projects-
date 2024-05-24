import math
import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ZERO = 0
timer_t = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_t)
    art.itemconfig(canvas, text=f"00:00")
    timer.config(text='Timer', bg=YELLOW, font=(FONT_NAME, 35, 'bold'), fg=GREEN)
    global ZERO
    ZERO = 0


# TIMER MECHANISM
def start_timer():
    global ZERO
    ZERO += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if ZERO % 8 == 0:
        timer.config(text='Break', bg=YELLOW, font=(FONT_NAME, 35, 'bold'), fg=RED)
        tmr(long_break)

    elif ZERO % 2 == 0:
        timer.config(text='Break', bg=YELLOW, font=(FONT_NAME, 35, 'bold'), fg=PINK)
        tmr(short_break)
    else:
        timer.config(text='Work', bg=YELLOW, font=(FONT_NAME, 35, 'bold'), fg=GREEN)
        tmr(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def tmr(count):
    check.config(bg=YELLOW, fg=GREEN)
    sec = count % 60
    min = math.floor(count / 60)
    if min < 10 and sec < 10:
        art.itemconfig(canvas, text=f"0{min}:0{sec}")
    elif min < 10:
        art.itemconfig(canvas, text=f"0{min}:{sec}")
    elif sec >= 10:
        art.itemconfig(canvas, text=f"{min}:{sec}")
    else:
        art.itemconfig(canvas, text=f"{min}:0{sec}")
        if count > 0:
            global timer_t
            timer_t = window.after(1000, tmr, count - 1)

        else:
            start_timer()
            check.config(bg=YELLOW, fg=GREEN, variable=var, offvalue=0, onvalue='off')
            time.sleep(1)
            return


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text='Timer', bg=YELLOW, font=(FONT_NAME, 35, 'bold'), fg=GREEN)
timer.pack()

art = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file='tomato.png')
art.create_image(100, 112, image=tomato_png)
canvas = art.create_text(100, 130, text=f"{00}:{00}", fill='white', font=(FONT_NAME, 35, 'bold'))
art.pack()
var = StringVar()
check = Checkbutton(bg=YELLOW, fg=GREEN)
check.pack()


def create_n():
    start_timer()


def reseting():
    reset_timer()


start = Button(text='Start', command=create_n)
start.place(x=-20, y=270)

reset = Button(text='Reset', command=reseting)
reset.place(x=180, y=270)

window.mainloop()
