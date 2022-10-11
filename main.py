# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro Timer", fg=GREEN, bg=YELLOW)
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Long break", fg=RED)
        count_down(long_break_time)
    elif reps % 2 == 0:
        title_label.config(text="Short break", fg=PINK)
        count_down(short_break_time)
    else:
        title_label.config(text="Time to Work", fg=GREEN)
        count_down(work_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    global mark
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=95, pady=45, bg=YELLOW)
window.minsize(950, 400)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_bg = PhotoImage(file="11 pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_bg)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white"
)
canvas.grid(column=1, row=1)


title_label = Label(
    text="Pomodoro Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW
)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", font=("Arial", 12), command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", font=("Arial", 12), command=reset_timer)
reset_button.grid(column=2, row=3)

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25))
check_marks.grid(column=1, row=3)


window.mainloop()
