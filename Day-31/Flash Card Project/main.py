from tkinter import *
from typing import ChainMap
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#---------------------------------------SAVING THE DATA--------------------------------#

def is_known():
    to_learn.remove(card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv", index=False)

#--------------------------------------FLASHING THE CARD-------------------------------#

def flip_card():
    global card
    canvas.itemconfig(set_image, image=image_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")

#-------------------------READING THE DATA and SETTING UP THE BUTTONS------------------#

def next_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=card["French"], fill="black")
    canvas.itemconfig(set_image, image=image_front)
    flip_timer = window.after(3000, flip_card)

#--------------------------------------------UI SETUP----------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")
set_image = canvas.create_image(400, 263, image=image_front)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40,  "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60,  "bold"))
canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file="images/wrong.png")
x_btn = Button(image=x_image, highlightthickness=0, command=next_card)
x_btn.grid(row=1, column=0)

y_image = PhotoImage(file="images/right.png")
y_btn = Button(image=y_image, highlightthickness=0, command=is_known)
y_btn.grid(row=1, column=1)

next_card()

window.mainloop()