import tkinter as tk
from tkinter import messagebox
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Madrid", "Berlin", "Paris"],
        "correct_answer": "Paris",
        "type": "multiple_choice",
    },
    {
        "question": "Which programming language is known for its readability?",
        "correct_answer": "Python",
        "type": "fill_in_the_blank",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Venus", "Jupiter"],
        "correct_answer": "Jupiter",
        "type": "multiple_choice",
    },
    {
        "question": "What is the capital of Japan?",
        "correct_answer": "Tokyo",
        "type": "fill_in_the_blank",
    },
    {
        "question": "How many continents are there?",
        "options": ["5", "6", "7"],
        "correct_answer": "7",
        "type": "multiple_choice",
    },
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(root, textvariable=self.answer_var, font=("Helvetica", 12))
        self.answer_entry.pack(pady=5)

        self.check_answer_button = tk.Button(root, text="Check Answer", command=self.check_answer)
        self.check_answer_button.pack(pady=10)
        self.check_answer_button.config(state=tk.DISABLED)

        self.next_question_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_question_button.pack(pady=10)
        self.next_question_button.config(state=tk.DISABLED)
      
        self.option_buttons = []

        self.load_question(0)

    def load_question(self, question_num):
        if question_num < len(quiz_data):
            question_data = quiz_data[question_num]
            self.question_label.config(text=question_data["question"])

            self.destroy_option_buttons()
            self.answer_var.set("")

            if question_data.get("options"):
                self.answer_entry.config(state=tk.DISABLED)
                for option in question_data["options"]:
                    option_button = tk.Button(self.root, text=option, command=lambda o=option: self.check_answer(o))
                    option_button.pack()
                    self.option_buttons.append(option_button)
            else:
                self.answer_entry.config(state=tk.NORMAL)
                self.check_answer_button.config(state=tk.NORMAL)
        else:
            self.show_final_score()

    def destroy_option_buttons(self):
        for button in self.option_buttons:
            button.destroy()
        self.option_buttons = []

    def check_answer(self, user_answer=None):
        current_question_data = quiz_data[self.current_question]
        if user_answer is None:
            user_answer = self.answer_var.get()
        correct_answer = current_question_data["correct_answer"]

        if user_answer.lower() == correct_answer.lower():
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Wrong! Correct answer: {correct_answer}", fg="red")

        self.next_question_button.config(state=tk.NORMAL)
        self.check_answer_button.config(state=tk.DISABLED)

    def next_question(self):
        self.current_question += 1
        self.feedback_label.config(text="")
        self.next_question_button.config(state=tk.DISABLED)
        self.check_answer_button.config(state=tk.DISABLED)

        if self.current_question < len(quiz_data):
            self.load_question(self.current_question)
        else:
            self.show_final_score()

    def show_final_score(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(quiz_data)}")
        self.root.quit()


root = tk.Tk()
app = QuizApp(root)

root.mainloop()
