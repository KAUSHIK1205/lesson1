import tkinter as tk

def convert():
    cm = float(entry.get())
    feet = cm / 30.48
    label_result.config(text=f"{cm} cm = {feet:.2f} feet")

root = tk.Tk()
root.title("Length Converter")
tk.Label(root, text="Enter length in cm:").pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Convert to Feet", command=convert).pack(pady=5)
label_result = tk.Label(root, text="")
label_result.pack()
root.mainloop()