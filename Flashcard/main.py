import random
import time
from tkinter import *
import pandas as pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def know_word():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=fc_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=fc_back_img)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])

window = Tk()
window.title("Flash Card")
window.config(background=BACKGROUND_COLOR, highlightthickness=0, pady=30, padx=30)
fc_front_img = PhotoImage(file="images/card_front.png")
fc_back_img = PhotoImage(file="images/card_back.png")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=850, height=550)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(430,280,image=fc_front_img)
card_title = canvas.create_text(425, 150, text="title", font=("Ariel", 48, "italic"))
card_word = canvas.create_text(425, 300, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=1, columnspan=3)

right_btn_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, command=know_word)
right_btn.grid(row=1,column=3)

wrong_btn_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0)
wrong_btn.grid(row=1, column=1)

next_card()


window.mainloop()
