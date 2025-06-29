import tkinter as tk
from tkinter import ttk

def show_result(score, total):
    result_win = tk.Toplevel()
    result_win.title("Result")
    result_win.geometry("300x200")
    result_win.config(bg="#e0ffe0")


    label = ttk.Label(result_win, text=f"You scored {score} out of {total}!", font=("Arial", 16))
    label.pack(pady=40)

    close_btn = ttk.Button(result_win, text="Close", command=result_win.destroy)
    close_btn.pack()
