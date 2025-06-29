import tkinter as tk
from tkinter import ttk
import json
from quiz import QuizWindow
from result import show_result
# done
with open("questions.json", "r") as f:
    topics = json.load(f)

# Function to choose topic choice
def choose_topic(root):
    win = tk.Toplevel(root)
    win.title("Choose a Topic")
    win.geometry("400x300")
    win.config(bg="#f9f9f9")

    ttk.Label(win, text="Select Topic", font=("Arial", 16, "bold")).pack(pady=20)

    def start_topic_quiz(topic_name):
        selected_questions = topics.get(topic_name, [])
        if selected_questions:
            win.destroy()
            QuizWindow(root, show_result, selected_questions)

    for topic in topics:
        if topic != "Default":  # Skip the default quiz entry
            ttk.Button(win, text=topic, command=lambda t=topic: start_topic_quiz(t)).pack(pady=10)
