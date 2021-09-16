import tkinter
from typing import Text
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#fafafa"
score = 0
#font=('Arial', 20, 'italic'
class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Qiuzzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
       
        self.label = tkinter.Label(text=f'Score: {score }', font=('Arial', 10), bg=THEME_COLOR)
        self.label.config(foreground='white')
        self.label.grid(column=1, row=0)
        self.canvas = tkinter.Canvas(width=300, height=250, bg=WHITE, highlightthickness=0)
        self.question_label = self.canvas.create_text(150, 125, text="sample", width=280, fill = THEME_COLOR, font=('Arial', 15, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan = 2, pady=50)

        self.rigth_image = tkinter.PhotoImage(file = '/home/levi/Documents/website/100 days of python/quizzler-app-start/images/true.png' )
        self.rigth = tkinter.Button(pady = -5, image=self.rigth_image, highlightthickness=0,command= self.right)
        self.rigth.grid(row=2, column=0)

        self.wrong_image = tkinter.PhotoImage(file = '/home/levi/Documents/website/100 days of python/quizzler-app-start/images/false.png' )
        self.wrong = tkinter.Button(pady = -5,image=self.wrong_image, highlightthickness=0, command= self.wrong)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text = q_text)

        else:
            self.canvas.itemconfig(self.question_label, text="You've reached the end of the quiz.")
            self.rigth.config(state="disabled")
            self.wrong.config(state="disabled")
    def right(self):
        self.get_feedback(self.quiz.check_answer('true'))   

    def wrong(self):
        self.get_feedback(self.quiz.check_answer('false'))  

    def get_feedback(self,is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)