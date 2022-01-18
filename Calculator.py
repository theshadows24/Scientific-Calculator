from tkinter import *
root = Tk()
root.geometry("400x360+400+150")
root.title("Calculator")
temp = ''
op = ''
mystr1 = StringVar()
mystr1.set("")
e1 = Entry(root, textvariable=mystr1, justify='right', font=('DSEG7 Classic',35)).place(height=60, width=400, x=0, y=0)

def clr():
    mystr1.set('')
    
def zero():
    txt = mystr1.get()
    txt = txt + '0'
    mystr1.set(txt)
    
def one():
    txt = mystr1.get()
    txt = txt + '1'
    mystr1.set(txt)
    
def two():
    txt = mystr1.get()
    txt = txt + '2'
    mystr1.set(txt)
    
def three():
    txt = mystr1.get()
    txt = txt + '3'
    mystr1.set(txt)

def add():
    global temp
    temp = mystr1.get()
    global op
    op = '+'
    mystr1.set('')

def minu():
    global temp
    temp = mystr1.get()
    global op
    op = '-'
    mystr1.set('')
    
def eq():
    txt = int(mystr1.get())
    if op == '+':
        txt = txt + int(temp)
    if op == '-':
        txt = int(temp) - txt
    mystr1.set(str(txt))



b = Button(root, text="CLR", command=clr).place(height=60, width =300, x=0, y=60)
b = Button(root, text="/").place(height=60, width =100, x=300, y=60)

b = Button(root, text="7").place(height=60, width =100, x=0, y=120)
b = Button(root, text="8").place(height=60, width =100, x=100, y=120)
b = Button(root, text="9").place(height=60, width =100, x=200, y=120)
b = Button(root, text="x").place(height=60, width =100, x=300, y=120)

b = Button(root, text="4").place(height=60, width =100, x=0, y=180)
b = Button(root, text="5").place(height=60, width =100, x=100, y=180)
b = Button(root, text="6").place(height=60, width =100, x=200, y=180)
b = Button(root, text="-", command=minu).place(height=60, width =100, x=300, y=180)

b = Button(root, text="1", command=one).place(height=60, width =100, x=0, y=240)
b = Button(root, text="2", command=two).place(height=60, width =100, x=100, y=240)
b = Button(root, text="3", command=three).place(height=60, width =100, x=200, y=240)
b = Button(root, text="+", command=add).place(height=120, width =100, x=300, y=240)

b = Button(root, text=".").place(height=60, width =100, x=0, y=300)
b = Button(root, text="0", command=zero).place(height=60, width =100, x=100, y=300)
b = Button(root, text="=", command=eq).place(height=60, width =100, x=200, y=300)



root.mainloop()