from tkinter import *
from tkinter import messagebox
from tkinter import font
import math as m
root = Tk()
root.title("Calculator")
root.iconbitmap("Calculator.ico")
root.configure(background="#2b2d42")
root.resizable(False,False)

my_font = font.Font(size=14)

entry = Entry(root, width=30, font=("arial", 20, "bold"), justify=RIGHT, bd=4)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# --------------------------------- Functions ---------------------------

def button_click(number):
    old = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(old) + str(number))


def clear():
    entry.delete(0,END)


def button_equal():
    val = entry.get()
    val = eval(val)
    entry.delete(0,END)
    entry.insert(0,val)

def button_sqrt():
    num = int(entry.get())
    entry.delete(0,END)
    result = m.sqrt(num)
    entry.insert(0,result)
# --------------------------------- Buttons -----------------------------

btn1 = Button(root, text="AC", width=10, height=3, borderwidth=0, bg="#ffb703", command= clear)
btn2 = Button(root, text="√", width=10, height=3, borderwidth=0, bg="#ffb703", command= button_sqrt)
btn3 = Button(root, text="mod", width=10, height=3, borderwidth=0, bg="#ffb703", command= lambda: button_click('%'))
btn4 = Button(root, text="÷", width=10, height=3, borderwidth=0, bg="#fb8500", command= lambda: button_click('/'))
btn5 = Button(root, text="7", width=10, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click(7))
btn6 = Button(root, text="8", width=10, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click(8))
btn7 = Button(root, text="9", width=10, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click(9))
btn8 = Button(root, text="×", width=10, height=3, borderwidth=0, bg="#fb8500", command= lambda: button_click('*'))
btn9 = Button(root, text="4", width=10, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click(4))
btn10 = Button(root,text="5", width=10, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click(5))
btn11 = Button(root, text="6", width=10, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click(6))
btn12 = Button(root, text="-", width=10, height=3, borderwidth=0, bg="#fb8500", command= lambda: button_click('-'))
btn13 = Button(root, text="1", width=10, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click(1))
btn14 = Button(root, text="2", width=10, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click(2))
btn15 = Button(root, text="3", width=10, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click(3))
btn16 = Button(root, text="+", width=10, height=3, borderwidth=0, bg="#fb8500", command= lambda: button_click('+'))
btn17 = Button(root, text="0", width=21, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click(0))
btn18 = Button(root, text="•", width=10, height=3, borderwidth=0, bg="#cbc0d3", command= lambda: button_click('•'))
# btn19 = Button(root, text="=", width=10, height=3, borderwidth=0, bg="#bdb2ff")
btn20 = Button(root, text="=", width=10, height=3, borderwidth=0, bg="#fb8500", command= button_equal)


btn1['font'] = my_font
btn2['font'] = my_font
btn3['font'] = my_font
btn4['font'] = my_font
btn5['font'] = my_font
btn6['font'] = my_font
btn7['font'] = my_font
btn8['font'] = my_font
btn9['font'] = my_font
btn10['font'] = my_font
btn11['font'] = my_font
btn12['font'] = my_font
btn13['font'] = my_font
btn14['font'] = my_font
btn15['font'] = my_font
btn16['font'] = my_font
btn17['font'] = my_font
btn18['font'] = my_font
# btn19['font'] = my_font
btn20['font'] = my_font


btn1.grid(row=1, column=0, pady=1, padx=1)
btn2.grid(row=1, column=1, padx=1)
btn3.grid(row=1, column=2, padx=1)
btn4.grid(row=1, column=3, padx=1)
btn5.grid(row=2, column=0, pady=1)
btn6.grid(row=2, column=1)
btn7.grid(row=2, column=2)
btn8.grid(row=2, column=3)
btn9.grid(row=3, column=0, pady=1)
btn10.grid(row=3, column=1)
btn11.grid(row=3, column=2)
btn12.grid(row=3, column=3)
btn13.grid(row=4, column=0, pady=1)
btn14.grid(row=4, column=1)
btn15.grid(row=4, column=2)
btn16.grid(row=4, column=3)
btn17.grid(row=5, column=0, pady=1, columnspan=2)
btn18.grid(row=5, column=2)
# btn19.grid(row=5, column=2)
btn20.grid(row=5, column=3)



mainloop()
