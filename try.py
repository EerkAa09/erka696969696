import tkinter as tk

def darakh(utga):
    delgets.insert(tk.END, utga)

def tseverleh():
    delgets.delete(0, tk.END)

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

delgets = tk.Entry(root, font=("Arial", 20), justify="right")
delgets.pack(fill="both", padx=10, pady=10, ipady=10)

tovchluuruud = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

for mor in tovchluuruud:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for tovch in mor:
        if tovch == "=":
            btn = tk.Button(frame, text=tovch, font=("Arial", 18),
                            command=bodoh)
        else:
            btn = tk.Button(frame, text=tovch, font=("Arial", 18),
                            command=lambda t=tovch: darakh(t))
        btn.pack(side="left", expand=True, fill="both")

clear_btn = tk.Button(root, text="C", font=("Arial", 18),
                      command=tseverleh)
clear_btn.pack(fill="both", padx=10, pady=5)

root.mainloop()
