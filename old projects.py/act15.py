import tkinter as tk
import random

def play(choice):
    options = ['Rock', 'Paper', 'Scissor']
    comp = random.choice(options)
    win = (choice == 'Rock' and comp == 'Scissor') or \
          (choice == 'Paper' and comp == 'Rock') or \
          (choice == 'Scissor' and comp == 'Paper')
    if choice == comp:
        msg = f"Computer chose {comp}. It's a tie."
    elif win:
        msg = f"Computer chose {comp}. I hate when I win 😤"
    else:
        msg = f"Computer chose {comp}. Computer wins."
    label_result.config(text=msg)

root = tk.Tk()
root.title("Rock Paper Scissor")
label_result = tk.Label(root, text="Choose your move!", font=("Arial", 14))
label_result.pack(pady=10)
for move in ['Rock', 'Paper', 'Scissor']:
    tk.Button(root, text=move, width=15, command=lambda m=move: play(m)).pack(pady=5)
root.mainloop()