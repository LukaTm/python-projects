from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"



class QuizInterface:


    def __init__(self,quiz_brain: QuizBrain ): # Makes to so it knows what quiz_brain is from and only takes those inputs from there
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.text = Label(text="Score: 0",background=THEME_COLOR,fg='white',font=('bald'))
        self.text.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250)
        self.question_text = self.canvas.create_text(150,125,width=280,text="Some Question Text",fill=THEME_COLOR,font=("Arial",20,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image,highlightthickness=0,command=self.false)
        self.true_button.grid(row=2,column=0)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image,highlightthickness=0,command=self.true)
        self.false_button.grid(row=2,column=1)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.text.config(text=f"Score: {self.quiz.score}")
            q_test = self.quiz.next_question() # LOOK ABOVE FOR COMMENT EXPLAINED TO HOW SHOW THIS
            self.canvas.itemconfig(self.question_text,text=q_test)
        else:
            self.canvas.itemconfig(self.question_text, text="Youve reached the end goodbye bia")
            self.true_button.config(state='disabled') # DISABLES BUTTONS
            self.false_button.config(state='disabled')

    def true(self):
        self.give_feedback(self.quiz.check_answer("True")) # same line

    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right) # same line
    def give_feedback(self,is_right):
        if is_right: # Ja nav true answer
            self.canvas.config(bg='green',highlightthickness=0)
        else:
            self.canvas.config(bg='red',highlightthickness=0)
        self.window.after(1000,self.get_next_question)







