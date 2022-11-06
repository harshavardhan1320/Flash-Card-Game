import pandas
import random
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

data = pandas.read_csv("Book.csv")
del data["Unnamed"]
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Book.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_question():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Kannada", fill="black")
    canvas.itemconfig(card_word, text=current_card["KANNADA"], fill="black")
    canvas.itemconfig(card_n_word, text=current_card["Read In KANNADA"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(5000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_question()


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["ENGLISH"], fill="white")
    canvas.itemconfig(card_n_word, text="")



window = Tk()
window.title("Flash card")
window.configure(padx=50, pady=50, background=BACKGROUND_COLOR, height=600, width=800)
flip_timer = window.after(5000, func=flip_card)

# creating canvas at background
canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 120, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 233, text="", font=("Ariel", 60, "bold"))
card_n_word = canvas.create_text(400, 350, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# creating wrong button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, background="white", command=next_question)
wrong_button.grid(row=1, column=0)

# creating right button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, background="white", command=is_known)
right_button.grid(row=1, column=1)









next_question()

window.mainloop()
