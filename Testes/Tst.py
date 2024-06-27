import tkinter as tk
from tkinter import ttk

window = tk.Tk()

def handle_click(event):
    print("The button was clicked!")
    button = tk.Button(text="Click me!",master=frame1)
    button.pack()

button_d = tk.Button(text="Click me!")

button_d.bind("<Button-1>", handle_click)
button_d.pack()

greeting = tk.Label(text="Hello, Tkinter", foreground='black',background='#34A2FE',width=10,height=2)
bt = tk.Button(text="Hello, Tkinter", foreground='black',background='#34A2FE',width=10,height=2)
entry = tk.Entry(fg="yellow", bg="#34A2FE", width=50)
text = tk.Text(fg="yellow", bg="#34A2FE", width=50,height=6)
entry.pack()
greeting.pack()
bt.pack()
text.pack()

border_effects = {

    "flat": tk.FLAT,

    "sunken": tk.SUNKEN,

    "raised": tk.RAISED,

    "groove": tk.GROOVE,

    "ridge": tk.RIDGE,

}

for relief_name, relief in border_effects.items():

    frame = tk.Frame(master=window, relief=relief, borderwidth=5)

    frame.pack()

    label = tk.Label(master=frame, text=relief_name)

    label.pack()


frame1 = tk.Frame(master=window, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=60,bg="blue")
frame3.pack(fill=tk.BOTH,side='left',expand=True)

frame = tk.Frame(master=window, width=150, height=150)

frame.pack()


label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")

label1.place(x=0, y=0)


label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")

label2.place(x=75, y=75)

window.mainloop()
