from tkinter import *
import flet as ft

#--------------DECLARATION---------------
top = Tk()
top.geometry("400x400")

marginX = 53
marginY = 56
expr = ""
txt = StringVar()

myLabel = Label(top, textvariable=txt, bg='white', bd=4, height=3, width=29, relief=RIDGE, wraplength=150).place(x=0, y=0)

btns = [["AC", "Del", "(", ")"],
       [7, 8, 9, '÷'],
       [4, 5, 6, '×'],
       [1, 2, 3, '-'],
       ['.', 0, '=', '+']
]

def insert(arg):
    global expr
    if arg in ["AC", "Del", "÷", "×", "="]:
        if arg == "AC":
            expr = ""
        elif arg == "Del":
            expr = expr[0: -1]
        elif arg == "÷":
            expr += "/"
        elif arg == "×":
            expr += "*"
        elif arg == "=":
            expr = str(calc())
    else:
        expr += str(arg)

    #print(expr)
    txt.set(expr)

def calc():
    return eval(expr)

#TASK
for i in range(5):
    for j in range(4):
        Button(top, text=f'{btns[i][j]}', fg='blue', bd=3, height=3, activebackground="grey", width=6, command=lambda i=i, j=j: insert(btns[i][j])).place(x=marginX*j, y=marginY*(i+1))


top.mainloop()