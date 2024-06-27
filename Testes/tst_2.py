import tkinter as tk
from tkinter import ttk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=100, minsize=100)
    window.rowconfigure(i, weight=1, minsize=80)


for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j,padx=10,pady=6)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=10,pady=10)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="n")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="n")


window.mainloop()