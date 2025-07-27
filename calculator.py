
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("calculator")
window.geometry("400x600")
#functions
def buttonClick(value):
    x = displayVar.get()
    displayVar.set(x+value)
def calculate():
    try :
        y = eval(displayVar.get())
        displayVar.set(y)
    except Exception as e:
        displayVar.set(e)
#display
displayVar = tk.StringVar()
display = ttk.Entry(window,textvariable = displayVar , font = ("arial" ,24 ),justify= "right")
display.grid(row=0 , column=0 ,columnspan =4 , sticky ="ewns" ,padx=5,pady=5)

#buttons
button_one = ttk.Button(window,text="1",command= lambda : buttonClick('1'))
button_one.grid(row = 1, column=0, padx=5, pady=5 , sticky ="ewns")
button_two = ttk.Button(window,text="2",command= lambda : buttonClick('2'))
button_two.grid(row = 1, column=1, padx=5, pady=5 , sticky ="ewns")
button_three = ttk.Button(window,text="3",command= lambda : buttonClick('3'))
button_three.grid(row = 1, column=2, padx=5, pady=5 , sticky ="ewns")
button_eraser = ttk.Button(window,text="/",command= lambda : buttonClick('/'))
button_eraser.grid(row = 1, column=3, padx=5, pady=5 , sticky ="ewns")
button_four = ttk.Button(window,text="4",command= lambda : buttonClick('4'))
button_four.grid(row = 2, column=0, padx=5, pady=5 , sticky ="ewns")
button_five = ttk.Button(window,text="5",command= lambda : buttonClick('5'))
button_five.grid(row = 2, column=1, padx=5, pady=5 , sticky ="ewns")
button_six = ttk.Button(window,text="6",command= lambda : buttonClick('6'))
button_six.grid(row = 2, column=2, padx=5, pady=5 , sticky ="ewns")
button_add = ttk.Button(window,text="+",command= lambda : buttonClick('+'))
button_add.grid(row = 2, column=3, padx=5, pady=5 , sticky ="ewns")
button_seven = ttk.Button(window,text="7",command= lambda : buttonClick('7'))
button_seven.grid(row = 3, column=0, padx=5, pady=5 , sticky ="ewns")
button_eight =  ttk.Button(window,text="8",command= lambda : buttonClick('8'))
button_eight.grid(row = 3, column=1, padx=5, pady=5 , sticky ="ewns")
button_nine = ttk.Button(window,text="9",command= lambda : buttonClick('9'))
button_nine.grid(row = 3, column=2, padx=5, pady=5 , sticky ="ewns")
button_multiply = ttk.Button(window,text="x",command= lambda : buttonClick('x'))
button_multiply.grid(row = 3, column=3, padx=5, pady=5 , sticky ="ewns")
button_zero = ttk.Button(window,text="0",command= lambda : buttonClick('0'))
button_zero.grid(row = 4, column=0, padx=5, pady=5 , sticky ="ewns")
button_dot = ttk.Button(window,text=".",command= lambda : buttonClick('.'))
button_dot.grid(row = 4, column=1, padx=5, pady=5 , sticky ="ewns")
button_equalto = ttk.Button(window,text="=",command=calculate)
button_equalto.grid(row = 4, column=3, padx=5, pady=5 , sticky ="ewns")
button_minus = ttk.Button(window,text="-",command= lambda : buttonClick('-'))
button_minus.grid(row = 4, column=2, padx=5, pady=5 , sticky ="ewns")
button_clear = ttk.Button(window,text="AC",command= lambda : displayVar.set(""))
button_clear.grid(row = 5,columnspan=4 ,column=0, padx=5, pady=5 , sticky ="ewns")

for i in range(6):
    window.rowconfigure(i , weight=1)
for j in range(4):
    window.columnconfigure(j , weight=1)



window.mainloop()







