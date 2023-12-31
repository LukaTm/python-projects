from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv('data/word_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records') # orien="records" - only picks columns values neliek tur klat 0: un liek sita - [{'French': 'partie', 'English': 'part'},




def next_card():
    global current_card ,flip_timer # LEARN GLOBAL
    window.after_cancel(flip_timer) # cancels the timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill='black') # configures
    canvas.itemconfig(card_word, text=current_card["French"],fill='black')
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000,func=flip_card) # next_card it cancels out itself


def flip_card():
    canvas.itemconfig(card_title,text="English",fill='white') #text color - fill
    canvas.itemconfig(card_word,text=current_card["English"],fill= 'white')
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/word_to_learn.csv',index=False) #index False so it doesnt add index 012345566789 utt

    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card) # timer thingy

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400,526/2,image=card_front_img)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40, 'italic'))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))

canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image,highlightthickness=0,command=is_known)
know_button.grid(row=1,column=1)

next_card()






window.mainloop()

