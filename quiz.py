import tkinter as tk
from tkinter import ttk
import json
# seen 
# Load default questions from JSON
with open("questions.json", "r") as f:
    question_data = json.load(f)
    default_questions = question_data.get("Default", [])

class QuizWindow(tk.Toplevel):
    def __init__(self, parent, result_callback, questions_list=None):
        super().__init__(parent)
        self.title("Quiz")
        self.geometry("500x300")
        self.config(bg="#ffffff")
        self.result_callback = result_callback

        self.questions = questions_list or default_questions
        self.q_index = 0
        self.score = 0
        self.user_answer = tk.StringVar()

        self.question_label = ttk.Label(self, wraplength=450, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.options_frame = ttk.Frame(self)
        self.options_frame.pack()

        self.next_button = ttk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        self.user_answer.set("")
        q_data = self.questions[self.q_index]
        self.question_label.config(text=f"Q{self.q_index + 1}: {q_data['question']}")

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for opt in q_data["options"]:
            rb = ttk.Radiobutton(self.options_frame, text=opt, variable=self.user_answer, value=opt)
            rb.pack(anchor="w", pady=5)

    def next_question(self):
        if self.user_answer.get() == self.questions[self.q_index]["answer"]:
            self.score += 1
        self.q_index += 1
        if self.q_index < len(self.questions):
            self.load_question()
        else:
            self.destroy()
            self.result_callback(self.score, len(self.questions))
