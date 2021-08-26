from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class AppUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=30, pady=30)

        self.canvas = Canvas(width=300,height=330, bg="white")
        self.question = self.canvas.create_text(
            150, 
            165, 
            width=280,
            text="Who won the gold medal \nfor India in Olympics2020?", 
            font=("Ariel", 15,  "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        #Label
        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Ariel", 10,  "italic"), bg=THEME_COLOR, fg="white")
        self.score_label.config(padx=20, pady=25)
        self.score_label.grid(row=0, column=1)

        #Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.true_btn)
        self.true_button.grid(row=3, column=0)

        false_img = PhotoImage(file="images/false.png") 
        self.false_button = Button(image=false_img, command=self.false_btn)
        self.false_button.grid(row=3, column=1)

        self.next_question()
        
        self.window.mainloop()


    def next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text="End of Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_btn(self):
        self.feedback(is_right = self.quiz.check_answer("True"))


    def false_btn(self):
        self.feedback(is_right = self.quiz.check_answer("False"))

    def change_bg(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.window.after(1000, self.next_question)
        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, self.next_question)

    def feedback(self, is_right):
        self.window.after(100, self.change_bg, is_right)


