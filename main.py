import tkinter as tk
from tkinter import ttk
from quiz import QuizWindow
from result import show_result
from topic_selector import choose_topic
from instructions import show_instructions

# Function to launch the default quiz
def open_quiz():
    quiz_win = QuizWindow(root, show_result)

# Initialize main window
root = tk.Tk()
root.title("Quiz Quest")
root.geometry("400x400")
root.configure(bg="#e3a0a0")  # Light pink background


style = ttk.Style(root)
style.configure("TButton", font=("Segoe UI", 12), padding=10)
style.configure("TLabel", font=("Segoe UI", 18, "bold"), background="#d8f3dc")


title = ttk.Label(root, text="Quiz Quest", background="#d8f3dc")
title.pack(pady=40)


# Start the quiz using default questions from quiz.py
start_button = ttk.Button(root, text="Start Default Quiz", command=open_quiz)
start_button.pack(pady=10)

# Choose a topic for custom quiz (topic_selector.py)
topic_btn = ttk.Button(root, text="Choose Topic", command=lambda: choose_topic(root))
topic_btn.pack(pady=10)

# Show how to play instructions (instructions.py)
howto_btn = ttk.Button(root, text="How to Play", command=show_instructions)
howto_btn.pack(pady=10)

root.mainloop()
