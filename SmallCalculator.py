from tkinter import *

root=Tk()
root.title("Simple Calculator")
inputt = Entry(root,width=35,borderwidth=5)
inputt.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    #inputt.delete(0,END)
    current=inputt.get()
    inputt.delete(0,END)
    inputt.insert(0,str(current) + str(number))
def button_clear():
    inputt.delete(0, END)

def button_add():
 first_number= inputt.get()
 global f_num
 global math
 math = "+"
 f_num = int(first_number)
 inputt.delete(0 , END)
def button_eq():
     second_number = inputt.get()
     inputt.delete(0, END)
     if math == "+":
        inputt.insert(0, f_num + int(second_number))
     if math == "-":
         inputt.insert(0, f_num - int(second_number))
     if math == "*":
         inputt.insert(0, f_num * int(second_number))
     if math == "/":
        inputt.insert(0, f_num / int(second_number))
     if  math == "%":
         inputt.insert(0,  f_num % int(second_number))

def button_div():
    first_number = inputt.get()
    global f_num
    global math
    math = "/"

    f_num = int(first_number)
    inputt.delete(0, END)
def button_sub():
    first_number = inputt.get()
    global f_num
    global math
    math = "-"
    f_num = int(first_number)
    inputt.delete(0, END)
def button_mul():
    first_number = inputt.get()
    global f_num
    global math
    math =  "*"

    f_num = int(first_number)
    inputt.delete(0, END)
def button_mode():
    first_number  = inputt.get()
    global f_num
    global math
    math = "%"
    f_num = int(first_number)
    inputt.delete(0,END)
# Define Buttons
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2=Button(root,text="2",padx=46,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3",padx=47,pady=20,command=lambda: button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5=Button(root,text="5",padx=46,pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6",padx=47,pady=20,command=lambda: button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(root,text="8",padx=46,pady=20,command=lambda: button_click(8))
button_9=Button(root,text="9",padx=47,pady=20,command=lambda: button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_equal=Button(root,text="=",command=button_eq,padx=100,pady=20)
clear=Button(root,text="C",command= button_clear,padx=47,pady=20)
button_plus = Button(root,text="+",padx=40,pady=20,command= button_add)
button_sub = Button(root,text="-",padx=46,pady=20,command= button_sub)
button_div = Button(root,text="/",padx=47,pady=20,command= button_div)
button_mul = Button(root,text="*",padx=40,pady=20,command= button_mul)
button_module = Button(root,text="%",padx=44,pady=20,command= button_mode)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)

clear.grid(row=4,column=2)
button_module.grid(row=4,column=1)
button_plus.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_mul.grid(row=6,column=0)
button_sub.grid(row=6, column=1)
button_div.grid(row=6,column=2)
root.mainloop()