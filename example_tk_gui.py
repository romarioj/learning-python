from tkinter import *

window = Tk()
window.title("Title Goes Here")

def lb_to_oz():
    print(e1_value.get())
    oz = float(e1_value.get())*16 #16 oz in 1 u.s. lb
    t1.insert(END,oz)

b1=Button(window,text="Calculate", command=lb_to_oz)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=0,column=2)


window.mainloop()
