from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ----- Data Management ---------
data = pandas.read_csv("translated_words.csv")
all_words = data.to_dict(orient='records')

current_word = None


def generate_new_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = all_words[random.choice(all_words)]
    card.itemconfig(card_image, image=front_img)
    card.itemconfig(language_label, text="Arabic", fill="#000000")
    card.itemconfig(word_label, text=current_word['arabic'], fill="#000000")
    flip_timer = window.after(3000, flip_card)


# ----- Managing events ---------
def flip_card():
    global current_word
    card.itemconfig(card_image, image=back_img)
    card.itemconfig(language_label, text="English", fill="#ffffff")
    card.itemconfig(word_label, text=current_word['english'], fill="#ffffff")


def right_click():
    all_words.remove(current_word)
    generate_new_word()


def wrong_click():
    generate_new_word()


# ----- UI Setup ---------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(400, 263, image=front_img)
card.grid(column=0, row=0, columnspan=2)

language_label = card.create_text(400, 150, text="Arabic", fill="black", font=("Ariel", 24, "italic"))
word_label = card.create_text(400, 263, text="Hello", fill="black", font=("Ariel", 40, "bold"))

# Control Buttons
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, bd=0, command=right_click)
right_btn.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, bd=0, command=wrong_click)
wrong_btn.grid(column=0, row=1)

flip_timer = window.after(3000, flip_card)
generate_new_word()

window.mainloop()
