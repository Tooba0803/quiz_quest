import tkinter as tk
from tkinter import ttk, messagebox
import json

# Load default questions safely
try:
    with open("questions.json", "r") as f:
        question_data = json.load(f)
        default_questions = question_data.get("Default", [])
except (FileNotFoundError, json.JSONDecodeError) as e:
    messagebox.showerror("Error", f"Failed to load questions.json: {e}")
    default_questions = []

class QuizWindow(tk.Toplevel):
    def __init__(self, parent, result_callback, questions_list=None):
        super().__init__(parent)
        self.title("Quiz")
        self.geometry("500x300")
        self.config(bg="#ffffff")

        self.result_callback = result_callback
        self.questions = questions_list or default_questions
        if not self.questions:
            messagebox.showerror("No Questions", "No questions available to display.")
            self.destroy()
            return

        self.q_index = 0
        self.score = 0
        self.user_answer = tk.StringVar()

        # Question label
        self.question_label = ttk.Label(self, wraplength=450, font=("Arial", 14))
        self.question_label.pack(pady=20)

        # Options container
        self.options_frame = ttk.Frame(self)
        self.options_frame.pack()

        # Next button
        self.next_button = ttk.Button(self, text="Next", command=self.next_question, state="disabled")
        self.next_button.pack(pady=20)

        # Track option selection
        self.user_answer.trace("w", self.on_option_selected)

        self.load_question()

    def load_question(self):
        """Load and display the current question and options"""
        self.user_answer.set("")
        q_data = self.questions[self.q_index]
        self.question_label.config(text=f"Q{self.q_index + 1}: {q_data['question']}")

        # Clear old options
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        # Display new options
        for opt in q_data["options"]:
            rb = ttk.Radiobutton(self.options_frame, text=opt, variable=self.user_answer, value=opt)
            rb.pack(anchor="w", pady=5)

        self.next_button.config(state="disabled")

    def on_option_selected(self, *args):
        """Enable the 'Next' button once an option is selected"""
        if self.user_answer.get():
            self.next_button.config(state="normal")

    def next_question(self):
        """Evaluate the current answer and load next question or finish"""
        if self.user_answer.get() == self.questions[self.q_index]["answer"]:
            self.score += 1

        self.q_index += 1
        if self.q_index < len(self.questions):
            self.load_question()
        else:
            self.destroy()
            self.result_callback(self.score, len(self.questions))

