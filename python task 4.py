#!/usr/bin/env python
# coding: utf-8

# In[1]:


# adding 2 numbers
def add(n1,n2):
    return(n1+n2)
    
#substracting 2 numbers
def sub(n1,n2):
    return(n1-n2)
    
#mutiplying 2 numbers
def mult(n1,n2):
    return(n1*n2)
    
#dividing 2 numbers
def dvd(n1,n2):
    if n2==0:
        return ("error! invalid operation")
    return(n1/n2)

def calculator():
    print('select operation')
    print('1.Adding')
    print('2.Substracting')
    print('3.Multiplying')
    print('4.Dividing')
    while True:
     ch=int(input("enter choice"))
     if ch in [1,2,3,4]:
         try:
             n1=int(input("enter n1"))
             n2=int(input("enter n2"))
         except ValurError:
             print("invalid input")
             continue
         if ch==1:
             print(n1 ,"+", n2 ,"=", {add(n1,n2)})
         if ch==2:
             print(n1 ,  "-", n2, "=", {sub(n1,n2)})
         if ch==3:
             print(n1 , "*", n2, "=", {mult(n1,n2)})
         if ch==4:
             r=dvd(n1,n2)
             if r=="error! invalid operation":
                print("can't perform operation")
             else:
             
                print(n1 , "/", n2 , "=", r)
     else: 
         print("invalid input option")

     nxcal=input("do u want to try once more ?")
     if nxcal.lower()=="no":
        break
if __name__ == "__main__":
    calculator()
         
                


# In[ ]:


# pip install tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator MAIN FLOW')
frame = tk.Frame(master=window, bg="white", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def myclick(number):
	entry.insert(tk.END, number)


def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear():
	entry.delete(0, tk.END)


button_1 = tk.Button(master=frame, text='1', padx=15,
					pady=5, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15,
					pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15,
					pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15,
					pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15,
					pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15,
					pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15,
					pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15,
					pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15,
					pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15,
					pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)

button_add = tk.Button(master=frame, text="+", padx=15,
					pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=5, column=0, pady=2)

button_subtract = tk.Button(
	master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=5, column=1, pady=2)

button_multiply = tk.Button(
	master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=5, column=2, pady=2)

button_div = tk.Button(master=frame, text="/", padx=15,
					pady=5, width=3, command=lambda: myclick('/'))
button_div.grid(row=6, column=0, pady=2)

button_clear = tk.Button(master=frame, text="clear",
						padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)

button_equal = tk.Button(master=frame, text="=", padx=15,
						pady=5, width=9, command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)

window.mainloop()


# 
