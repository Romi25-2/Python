# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Graphical user interface 
#pack one after the other 
#grid creates coordinates 
import tkinter as tk

def addition():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        answer = num1 + num2
        labelans.config(text=f"{answer}")
        labelans["bg"]="red"
        labelans["text"]=str(answer)
       
    except ValueError:
        labelans.config(text="Invalid input")
  
def subtraction():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        answer = num1 - num2
        labelans.config(text=f"{answer}")
        labelans["bg"]="red"
        labelans["text"]=str(answer)
       
    except ValueError:
        labelans.config(text="Invalid input")
        
calculate = tk.Tk()
calculate.title("Simple Calculater") 

label_num1 = tk.Label(calculate, text="Number 1:", bg="LightGreen")
label_num1.grid(row=0, column=0,padx=10,pady=5)

entry_num1 = tk.Entry(calculate, width=20)
entry_num1.grid(row=0, column=1, padx=10,pady=5)

label_num2 = tk.Label(calculate, text="Number 2:", bg="LightGreen")
label_num2.grid(row=1, column=0,padx=10,pady=5)

entry_num2 = tk.Entry(calculate, width=20)
entry_num2.grid(row=1, column=1, padx=10,pady=5)

labelans = tk.Label(calculate,text = "Answer:")
labelans.grid(row=4, column=0)

button_add = tk.Button(calculate, text="Add(+)", command = addition)
button_add.grid(row=2, column=0, padx=5,pady=10)

button_add = tk.Button(calculate, text="Subtrction(+)", command = subtraction)
button_add.grid(row=3, column=0, padx=5,pady=10)

calculate.mainloop()
