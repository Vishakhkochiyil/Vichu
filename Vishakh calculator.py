from tkinter import *
ep=""
def press(n):
    global ep
    ep=ep+str(n)
    eq.set(ep)
def equalto():
    try:
        global ep
        t=str(eval(ep))
        eq.set(t)
        ep=""
    except:
        eq.set("Errorrrrrrr")
        ep=""
def clear():
    global ep
    ep=""
    eq.set("")
    
        
t=Tk()
t.geometry('400x300')
t.title("Calculator")
eq=StringVar()
ex=Entry(t,textvariable=eq)
ex.grid(columnspan=10,ipadx=50,ipady=20,pady=10)
eq.set("Enter the number")

b1=Button(t,text="1",fg="yellow",bg="blue",command=lambda:press(1),height=2,width=10)
b1.grid(row=2,column=0)

b2=Button(t,text="2",fg="yellow",bg="blue",command=lambda:press(2),height=2,width=10)
b2.grid(row=2,column=1)

b3=Button(t,text="3",fg="yellow",bg="blue",command=lambda:press(3),height=2,width=10)
b3.grid(row=2,column=2)

b4=Button(t,text="4",fg="yellow",bg="blue",command=lambda:press(4),height=2,width=10)
b4.grid(row=3,column=0)

b5=Button(t,text="5",fg="yellow",bg="blue",command=lambda:press(5),height=2,width=10)
b5.grid(row=3,column=1)

b6=Button(t,text="6",fg="yellow",bg="blue",command=lambda:press(6),height=2,width=10)
b6.grid(row=3,column=2)

b7=Button(t,text="7",fg="yellow",bg="blue",command=lambda:press(7),height=2,width=10)
b7.grid(row=4,column=0)

b8=Button(t,text="8",fg="yellow",bg="blue",command=lambda:press(8),height=2,width=10)
b8.grid(row=4,column=1)

b9=Button(t,text="9",fg="yellow",bg="blue",command=lambda:press(9),height=2,width=10)
b9.grid(row=4,column=2)

b0=Button(t,text="0",fg="yellow",bg="blue",command=lambda:press(0),height=2,width=10)
b0.grid(row=5,column=0)

b0=Button(t,text="0",fg="yellow",bg="blue",command=lambda:press(0),height=2,width=10)
b0.grid(row=5,column=0)

plus=Button(t,text="+",fg="yellow",bg="blue",command=lambda:press("+"),height=2,width=10)
plus.grid(row=2,column=3)

minus=Button(t,text="-",fg="yellow",bg="blue",command=lambda:press("-"),height=2,width=10)
minus.grid(row=3,column=3)

multiply=Button(t,text="*",fg="yellow",bg="blue",command=lambda:press("*"),height=2,width=10)
multiply.grid(row=4,column=3)

divide=Button(t,text="/",fg="yellow",bg="blue",command=lambda:press("/"),height=2,width=10)
divide.grid(row=5,column=3)

equal=Button(t,text="=",fg="yellow",bg="blue",command=equalto,height=2,width=10)
equal.grid(row=5,column=2)

clear=Button(t,text="clear",fg="black",bg="white",command=clear,height=2,width=10)
clear.grid(row=5,column='1')

dot=Button(t,text=".",fg="yellow",bg="blue",command=lambda:press("."),height=2,width=10)
dot.grid(row=6,column=3)



















t.mainloop()
