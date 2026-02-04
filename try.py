import tkinter as tk

def darakh(utga):
    delgets.insert(tk.END, utga)



def bodoh():
    try:
        ur_dun = eval(delgets.get())
        delgets.delete(0, tk.END)
        delgets.insert(tk.END, ur_dun)
    except:
        delgets.delete(0, tk.END)
        delgets.insert(tk.END, "Алдаа")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Дэлгэц
delgets = tk.Entry(
    root,
    font=("Segoe UI", 22),
    justify="right",
    bg="#1e1e1e",
    fg="white",
    bd=0
)
delgets.pack(fill="both", padx=15, pady=15, ipady=10)

tovchluuruud = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

for mor in tovchluuruud:
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both", padx=5, pady=5)

    for tovch in mor:
        if tovch == "=":
            btn = tk.Button(
                frame,
                text=tovch,
                font=("Segoe UI", 16, "bold"),
                bg="#4caf50",
                fg="white",
                bd=0,
                command=bodoh
            )
        else:
            btn = tk.Button(
                frame,
                text=tovch,
                font=("Segoe UI", 16),
                bg="#2d2d2d",
                fg="white",
                bd=0,
                command=lambda t=tovch: darakh(t)
            )

        btn.pack(side="left", expand=True, fill="both", padx=4, pady=4)

# Clear товч
clear_btn = tk.Button(
    root,
    text="C",
    font=("Arial", 18),
    bg="#e53935",
    fg="white",
    bd=0,
    command=delgets.delete(0, tk.END)
)
clear_btn.pack(fill="both", padx=15, pady=10)

root.mainloop()
