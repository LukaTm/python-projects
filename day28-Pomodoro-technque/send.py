from tkinter import *
from playsound import playsound


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
import math

# ---------------------------- TIMER RESET ------------------------------- #
reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60
    if reps % 8 ==0:
        count_down(long_break_sec)
        timer_label.config(text="Break😎", fg=RED, font=('bold', 50))
        playsound('win.mp3')
    elif reps % 2 ==0:
        count_down(short_break_sec)
        timer_label.config(text="Break😲", fg=PINK, font=('bold', 50))
        playsound('win.mp3')
    else:
        count_down(work_sec)
        timer_label.config(text="Work😪",fg=GREEN, font=('bold',50))
        playsound('buhu.mp3')



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

a = 3
a = "Hello" # Dynamic Typing !!!!!!!!!!!!!!!!!!!!!!!


def count_down(count):
    count_min = math.floor(count /60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}') # to change canvas element
    if count > 0:
        window.after(1000,count_down,count-1)
    else:
        start_timer()





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("STRAT")
window.config(padx=100,pady=50,bg=YELLOW) # bg = bacground color



canvas = Canvas(width=205,height=224,bg=YELLOW,highlightthickness=0) # creates canvas where you can put picture
tomato_img = PhotoImage(file='fin.png') #created our tomato img cause below it needs it like this
canvas.create_image(103,113,image=tomato_img) # create image at this position(canvas) X AND y position we want it in middle
timer_text = canvas.create_text(103,130,text='00:00',fill='white',font=(FONT_NAME, 35,'bold'))
canvas.grid(row=1,column=1)



timer_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
timer_label.grid(row=0,column=1)

start_button = Button(text="Start",command=start_timer)
start_button.grid(row=3,column=0)

reset_button = Button(text="Reset")
reset_button.grid(row=3,column=2)

check_mark = Label(text="✔",bg=YELLOW,fg=GREEN,font=(FONT_NAME,12))
check_mark.grid(row=4,column=1)



window.mainloop()
