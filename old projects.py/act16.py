import tkinter as tk

def check_strength():
    pwd = entry.get()
    length = len(pwd)
    if length < 6:
        result = "Weak"
    elif length < 10:
        result = "Moderate"
    else:
        result = "Strong"
    label_result.config(text=f"Password Strength: {result}")

root = tk.Tk()
root.title("Password Strength Checker")
tk.Label(root, text="Enter Password:").pack()
entry = tk.Entry(root, show="*")
entry.pack()
tk.Button(root, text="Check Strength", command=check_strength).pack(pady=5)
label_result = tk.Label(root, text="")
label_result.pack()
root.mainloop()