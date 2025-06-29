import tkinter as tk
from tkinter import ttk

def show_instructions():
    win = tk.Toplevel()
    win.title("How to Play")
    win.geometry("400x300")
    win.config(bg="#fdfdfd")

    #instruction to play
    ttk.Label(win, text="🎮 How to Play the Quiz Game 🎮", font=("Arial", 14, "bold")).pack(pady=10)

    #motivational message
    ttk.Label(win, text="Good luck and have fun! 🧠", font=("Arial", 10, "italic")).pack()

    # Frame for grouped instructions
    frame = ttk.LabelFrame(win, text="Read Carefully", padding=10)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    
    instructions = (
        "1. Click 'Start Quiz' to begin.\n"
        "2. Select the correct answer from the options.\n"
        "3. Click 'Next' to go to the next question.\n"
        "4. At the end, your score will be shown.\n"
        "5. You can choose different topics from the topic page."
    )

  ttk.Label(win, text=instructions, wraplength=350, justify="left").pack(pady=20)
    ttk.Button(win, text="Close", command=win.destroy).pack(pady=10)

win.bind("<Escape>", lambda e: win.destroy())
