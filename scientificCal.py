#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
import math
window = Tk()
window.geometry("320x420") # size of the window width:- 500, height:- 375
window.resizable(0, 0) # this prevents from resizing the window
window.title("Scientific Calculator")
expression = ""
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result) 
    expression = ""
    

expression = ""
input_text = StringVar()

input_frame = Frame(window, width=312, height=50, bd = 0, highlightbackground = "black", highlightcolor = "black", 
                    highlightthickness = 1)

input_frame.grid(row=0,column=0)
input_field = Entry(input_frame, textvariable=input_text, font='Arial 18 bold', bg = '#eee', width=24,justify=RIGHT)
input_field.grid(row=0,column=0, columnspan=5, pady=2)
btns_frame = Frame(window, width=312, height=272.5 , bg = "grey")
btns_frame.grid(row=1,column=0)

clear = Button(btns_frame, text = "DEL", fg = "white", width = 21,  height = 3, bd = 0, bg = "#505B5B", 
               command = lambda: btn_clear()).grid(row = 0, column = 0,columnspan=2, padx = 1, pady = 1)

pi = Button(btns_frame, text = 'π', fg = 'white', width = 10, height = 3, bd = 0, bg = '#0B4F66',
                command = lambda: btn_click(3.14159)).grid(row = 0, column = 2, padx = 1, pady = 1)
log = Button(btns_frame, text = 'log', fg = 'white', width = 10, height = 3, bd = 0, bg = '#302F2F',
                command = lambda: btn_click('math.log')).grid(row = 0, column = 3, padx = 1, pady = 1)
square = Button(btns_frame, text = "x^2", fg = "white", width = 10, height = 3, bd = 0, bg = "#0B4F66",
                command = lambda: btn_click('**')).grid(row = 1, column = 0, padx = 1, pady = 1)
leftBracket = Button(btns_frame, text = "(", fg = "white", width = 10, height = 3, bd = 0, bg = "#0B4F66", 
               command = lambda: btn_click('(')).grid(row = 1, column = 1, padx = 1, pady = 1)
rightBracket = Button(btns_frame, text = ')', fg = "white", width = 10, height = 3, bd = 0, bg = "#0B4F66", 
              command = lambda: btn_click(')')).grid(row = 1, column = 2, padx = 1, pady = 1)
sqrt = Button(btns_frame, text = "√", fg = "white", width = 10, height = 3, bd = 0, bg = "#302F2F", 
                  command = lambda: btn_click("math.sqrt")).grid(row = 1, column = 3, padx = 1, pady = 1)
sin = Button(btns_frame, text = "sin", fg = "white", width = 10, height = 3, bd = 0, bg = "#0B4F66",
              command = lambda: btn_click('math.sin')).grid(row = 2, column = 0, padx = 1, pady = 1)
cos = Button(btns_frame, text = "cos", fg = "white", width = 10, height = 3, bd = 0, bg = "#0B4F66",
              command = lambda: btn_click('math.cos')).grid(row = 2, column = 1, padx = 1, pady = 1)
tan = Button(btns_frame, text = "tan", fg = "white", width = 10, height = 3, bd = 0, bg = "#0B4F66",
             command = lambda: btn_click('math.tan')).grid(row = 2, column = 2, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "white", width = 10, height = 3, bd = 0, bg = "#302F2F",
               command = lambda: btn_click("/")).grid(row = 2, column = 3, padx = 1, pady = 1)
seven = Button(btns_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "#212121", 
             command = lambda: btn_click(7)).grid(row = 3, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "#212121", 
             command = lambda: btn_click(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "#212121", 
               command = lambda: btn_click(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "white", width = 10, height = 3, bd = 0, bg = "#302F2F", 
              command = lambda: btn_click("*")).grid(row = 3, column = 3, padx = 1, pady = 1)
four = Button(btns_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "#212121", 
              command = lambda: btn_click(4)).grid(row = 4, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "#212121", 
               command = lambda: btn_click(5)).grid(row = 4, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "#212121", 
                command = lambda: btn_click(6)).grid(row = 4, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "#302F2F", 
                command = lambda: btn_click('-')).grid(row = 4, column = 3, padx = 1, pady = 1)
one = Button(btns_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "#212121", 
              command = lambda: btn_click(1)).grid(row = 5, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "#212121", 
               command = lambda: btn_click(2)).grid(row = 5, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "#212121", 
                command = lambda: btn_click(3)).grid(row = 5, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "white", width = 10, height = 3, bd = 0, bg = "#302F2F", 
                command = lambda: btn_click('+')).grid(row = 5, column = 3, padx = 1, pady = 1)
zero = Button(btns_frame, text = "0", fg = "white", width = 21, height = 3, bd = 0, bg = "#212121", 
              command = lambda: btn_click(0)).grid(row = 6, column = 0,columnspan=2 ,padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "#212121", 
               command = lambda: btn_click('.')).grid(row = 6, column = 2, padx = 1, pady = 1)
equalsto = Button(btns_frame, text = "=", fg = "white", width = 10, height = 3, bd = 0, bg = "#505B5B", 
                command = lambda: btn_equal()).grid(row = 6, column = 3, padx = 1, pady = 1)
window.mainloop()

