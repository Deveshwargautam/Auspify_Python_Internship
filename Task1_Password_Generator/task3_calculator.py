import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_value.set(result)
        except Exception as e:
            messagebox.showerror("Error", "गलत इनपुट!")
            screen_value.set("")
    elif text == "C":
        screen_value.set("")
    else:
        screen_value.set(screen.get() + text)

root = tk.Tk()
root.title("Auspify Calculator")
root.geometry("350x500")

screen_value = tk.StringVar()
screen_value.set("")

screen = tk.Entry(root, textvar=screen_value, font="lucida 28 bold", justify="right", bd=10, insertwidth=4, bg="powder blue")
screen.pack(fill=tk.BOTH, ipadx=8, ipady=10, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side=tk.TOP)
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="lucida 18 bold", padx=20, pady=20, width=3)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()
