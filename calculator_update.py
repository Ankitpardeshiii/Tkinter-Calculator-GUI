


import tkinter as tk
from tkinter import ttk
import math

# Creating main window
window = tk.Tk()
window.title("Calculator")
window.geometry("500x650")
window.configure(bg="#1e1e1e")  

# Functions
def buttonClick(value):
    current = displayVar.get()
    displayVar.set(current + str(value))

def clearDisplay():
    displayVar.set("")

def calculate():
    try:
        expression = displayVar.get().replace("x", "*")
        result = eval(expression)
        displayVar.set(result)
    except Exception:
        displayVar.set("Error")

def scientificFunction(func):
    try:
        expression = displayVar.get()
        if expression:
            value = float(expression)
            if func == "sqrt":
                result = math.sqrt(value)
            elif func == "sin":
                result = math.sin(math.radians(value))
            elif func == "cos":
                result = math.cos(math.radians(value))
            elif func == "tan":
                result = math.tan(math.radians(value))
            elif func == "log":
                result = math.log10(value)
            elif func == "ln":
                result = math.log(value)
            elif func == "exp":
                result = math.exp(value)
            displayVar.set(result)
    except Exception:
        displayVar.set("Error")

# Style configuration
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 14, "bold"), padding=10)
style.configure("Display.TEntry", font=("Arial", 28, "bold"), padding=10)

# Display
displayVar = tk.StringVar()
display = ttk.Entry(window, textvariable=displayVar, style="Display.TEntry", justify="right")
display.grid(row=0, column=0, columnspan=6, sticky="ewns", padx=8, pady=8)

# Button layout
buttons = [
    ('7',1,0,"#2d2d2d"), ('8',1,1,"#2d2d2d"), ('9',1,2,"#2d2d2d"), ('/',1,3,"#ff9800"), ('sqrt',1,4,"#4caf50"), ('^',1,5,"#4caf50"),
    ('4',2,0,"#2d2d2d"), ('5',2,1,"#2d2d2d"), ('6',2,2,"#2d2d2d"), ('x',2,3,"#ff9800"), ('sin',2,4,"#4caf50"), ('cos',2,5,"#4caf50"),
    ('1',3,0,"#2d2d2d"), ('2',3,1,"#2d2d2d"), ('3',3,2,"#2d2d2d"), ('-',3,3,"#ff9800"), ('tan',3,4,"#4caf50"), ('log',3,5,"#4caf50"),
    ('0',4,0,"#2d2d2d"), ('.',4,1,"#2d2d2d"), ('+',4,2,"#ff9800"), ('=',4,3,"#4caf50"), ('ln',4,4,"#4caf50"), ('exp',4,5,"#4caf50")
]

# Creating buttons 
for (text, r, c, color) in buttons:
    action = None
    if text in ['sqrt', 'sin', 'cos', 'tan', 'log', 'ln', 'exp']:
        action = lambda t=text: scientificFunction(t)
    elif text == '=':
        action = calculate
    elif text == '^':
        action = lambda: buttonClick("**")
    else:
        action = lambda t=text: buttonClick(t)

    btn = tk.Button(window, text=text, command=action, bg=color, fg="white",
                    font=("Arial", 14, "bold"), relief="flat")
    btn.grid(row=r, column=c, padx=5, pady=5, sticky="ewns")

# AC button
tk.Button(window, text="AC", command=clearDisplay, bg="#f44336", fg="white",
          font=("Arial", 14, "bold"), relief="flat").grid(row=5, column=0, columnspan=6, padx=5, pady=5, sticky="ewns")

# Resize grid
for i in range(6):
    window.columnconfigure(i, weight=1)
for j in range(6):
    window.rowconfigure(j, weight=1)

window.mainloop()






