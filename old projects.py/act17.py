import tkinter as tk

def calculate():
    p = float(entry_p.get())
    r = float(entry_r.get())
    t = float(entry_t.get())
    si = (p * r * t) / 100
    ci = p * ((1 + r / 100) ** t) - p
    label_result.config(text=f"Simple Interest: ₹{si:.2f}\nCompound Interest: ₹{ci:.2f}")

root = tk.Tk()
root.title("Interest Calculator")
tk.Label(root, text="Principal:").pack()
entry_p = tk.Entry(root)
entry_p.pack()
tk.Label(root, text="Rate (%):").pack()
entry_r = tk.Entry(root)
entry_r.pack()
tk.Label(root, text="Time (years):").pack()
entry_t = tk.Entry(root)
entry_t.pack()
tk.Button(root, text="Calculate", command=calculate).pack(pady=5)
label_result = tk.Label(root, text="")
label_result.pack()
root.mainloop()