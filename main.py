import tkinter as tk
from tkinter import ttk
from quiz import QuizWindow
from result import show_result
from topic_selector import choose_topic
from instructions import show_instructions

# Start default quiz (hardcoded questions from quiz.py)
def open_quiz():
    quiz_win = QuizWindow(root, show_result)

# Main window
root = tk.Tk()
root.title("Quiz Quest")
root.geometry("400x400")
root.configure(bg="#e3a0a0")  # Pastel pink background

# Styling
style = ttk.Style(root)
style.configure("TButton", font=("Segoe UI", 12), padding=10)
style.configure("TLabel", font=("Segoe UI", 18, "bold"), background="#d8f3dc")

# Title
title = ttk.Label(root, text="Quiz Quest", background="#d8f3dc")
title.pack(pady=40)

# Buttons
start_button = ttk.Button(root, text="Start Default Quiz", command=open_quiz)
start_button.pack(pady=10)

topic_btn = ttk.Button(root, text="Choose Topic", command=lambda: choose_topic(root))
topic_btn.pack(pady=10)

howto_btn = ttk.Button(root, text="How to Play", command=show_instructions)
howto_btn.pack(pady=10)

# Run the app
root.mainloop()
