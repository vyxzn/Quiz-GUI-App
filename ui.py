from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg= THEME_COLOR, padx= 20, pady= 20)

        self.scoreLabel = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR)
        self.scoreLabel.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.question = ""
        self.qText = self.canvas.create_text(150, 125, width=280, text=self.question, fill="white", font=('Ariel 20 italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady= 50)

        self.correctPicture = PhotoImage(file="images/true.png")
        self.correctBtn = Button(image=self.correctPicture, highlightthickness=0, command= self.check_right)
        self.correctBtn.grid(row=2, column=0)

        self.wrongPicture = PhotoImage(file="images/false.png")
        self.wrongBtn = Button(image=self.wrongPicture, highlightthickness=0, command= self.check_wrong)
        self.wrongBtn.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="black")
        if self.quiz.still_has_questions():
            self.scoreLabel.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.qText, text= q_text)
        else:
            self.canvas.itemconfig(self.qText, text=f"You have reached the end of the quiz. Score: {self.quiz.score}/10")
            self.correctBtn.config(state="disabled")
            self.wrongBtn.config(state="disabled")

    def check_right(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")

        else:
            self.canvas.config(bg = "red")

        self.window.after(1000, self.get_next_question)