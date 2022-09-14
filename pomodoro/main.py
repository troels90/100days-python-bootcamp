import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text="00:00")
        title_label.config(text="Timer")
        checkmark.config(text="")
        global reps
        reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    seconds = 0
    if reps == 8: #Long break timer
        seconds = LONG_BREAK_MIN * 60
        title_label.config(text="Break", fg=PINK)
    elif reps % 2 == 0: #Short break timer
        seconds = SHORT_BREAK_MIN * 60
        title_label.config(text="Break", fg=PINK)
    else:   #Work timer
       seconds = WORK_MIN * 60
       title_label.config(text="Work", fg=RED)
    count_down(seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    show_time = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=show_time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)    # milliseconds, function, parameters (*args)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark["text"] += "✔"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", command=start_timer)
reset_btn = Button(text="Reset", command=reset)
checkmark = Label(text="", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)

start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)
checkmark.grid(column=1, row=3)



window.mainloop()