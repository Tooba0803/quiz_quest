import tkinter as tk
from tkinter import ttk

def show_instructions():
    win = tk.Toplevel()
    win.title("How to Play")
    win.geometry("400x300")
    win.config(bg="#fdfdfd")

    #title 
    ttk.Label(win, text="🎮 How to Play the Quiz Game 🎮", font=("Arial", 14, "bold")).pack(pady=10)

    instructions = (
        "1. Click 'Start Quiz' to begin.\n"
        "2. Select the correct answer from the options.\n"
        "3. Click 'Next' to go to the next question.\n"
        "4. At the end, your score will be shown.\n"
        "5. You can choose different topics from the topic page."
    )

  ttk.Label(win, text=instructions, wraplength=350, justify="left").pack(pady=20)
    ttk.Button(win, text="Close", command=win.destroy).pack(pady=10)
