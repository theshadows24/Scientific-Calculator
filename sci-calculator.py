# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:06:26 2021

@author: Ifra
"""

#main
from tkinter import *
import math
import tkinter.messagebox

window = Tk()
window.title('Scientific Calculator')
window.configure(background = '#186CD4')
window.geometry('535x535')
#window.resizable(width=False,height=False)

expression = ""
def click(item):
    global expression
    expression = expression + str(item)
    exp.set(expression)

def clear():
    global expression
    expression = ""
    exp.set("0")
    
def equal():
    global expression
    try:
        total = str(eval(expression))
        exp.set(total)
        expression = ""
    except:
        messagebox.showerror('Error 404','Math ERROR \n For functions, be mindful of brackets. \n e.g. sin(90)')
        expression = ""
        


box = Frame(window, width=300, height=20, highlightbackground='#186CD4', highlightthickness=3)
box.grid(row=0,column=0, columnspan=2)

exp = StringVar()
exp.set('0')

ent = Entry(box, textvariable=exp, font='Arial 20 bold', bg = 'white', relief='ridge', bd=10, width=34,justify=RIGHT)
ent.grid(row=0,column=0, columnspan=7, pady=3)


btn = Frame(window, width=40, height=500, highlightbackground='#186CD4', highlightthickness=2)
btn.grid(row=1,column=0)

oper = Frame(window, width=300, height=500, highlightbackground='#186CD4', highlightthickness=2)
oper.grid(row=1, column=1)

brac1 = Button(btn, text='(', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click('('))
brac1.grid(row=0,column=0)
brac2 = Button(btn, text=')', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click(')'))
brac2.grid(row=0,column=1)
sqrt = Button(btn, text='√', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click('math.sqrt'))
sqrt.grid(row=0,column=2)
power = Button(btn, text='x^n', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click('**'))
power.grid(row=0,column=3)


seven = Button(btn, text='7', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(7))
seven.grid(row=1,column=0)
eight = Button(btn, text='8', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(8))
eight.grid(row=1,column=1)
nine = Button(btn, text='9', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(9))
nine.grid(row=1,column=2)

four = Button(btn, text='4', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(4))
four.grid(row=2,column=0)
five = Button(btn, text='5', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(5))
five.grid(row=2,column=1)
six = Button(btn, text='6', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(6))
six.grid(row=2,column=2)

one = Button(btn, text='1', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(1))
one.grid(row=3,column=0)
two = Button(btn, text='2', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(2))
two.grid(row=3,column=1)
three = Button(btn, text='3', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(3))
three.grid(row=3,column=2)

zero = Button(btn, text='0', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(0))
zero.grid(row=4,column=0)
point = Button(btn, text='.', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click('.'))
point.grid(row=4,column=1)

pi = Button(btn, text='𝝅', fg='black', bg='#A5C3D8', width=10, height=5, bd=5, command=lambda: click(3.14159))
pi.grid(row=4,column=2)


plus = Button(btn, text='+', fg='black', bg='#A5D8A8', width=10, height=5, bd=5, command=lambda: click('+'))
plus.grid(row=1,column=3)
minus = Button(btn, text='-', fg='black', bg='#A5D8A8', width=10, height=5, bd=5, command=lambda: click('-'))
minus.grid(row=2,column=3)
multiply = Button(btn, text='*', fg='black', bg='#A5D8A8', width=10, height=5, bd=5, command=lambda: click('*'))
multiply.grid(row=3,column=3)
divide = Button(btn, text='/', fg='black', bg='#A5D8A8', width=10, height=5, bd=5, command=lambda: click('/'))
divide.grid(row=4,column=3)


clr = Button(oper, text='CLR', fg='black', bg='#F9ABA4', width=22, height=5, bd=5, command=lambda: clear())
clr.grid(row=0,column=4, columnspan = 2)

sine = Button(oper, text='sin', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click('math.sin('))
sine.grid(row=1,column=4)
cosi = Button(oper, text='cos', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click('math.cos('))
cosi.grid(row=2,column=4)
tang = Button(oper, text='tan', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click('math.tan('))
tang.grid(row=3,column=4)
con_e = Button(oper, text='e', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click(2.71828))
con_e.grid(row=4,column=4)


rad = Button(oper, text='DEG', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click('math.radians('))
rad.grid(row=1,column=5)
log = Button(oper, text='log', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click('math.log('))
log.grid(row=2,column=5)
neg_pow = Button(oper, text='x^(-n)', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=lambda: click('**(-'))
neg_pow.grid(row=3,column=5)
eql = Button(oper, text='=', fg='black', bg='#C8B4B4', width=10, height=5, bd=5, command=equal)
eql.grid(row=4,column=5)


window.mainloop()