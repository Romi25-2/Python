# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 09:27:43 2025

@author: ROPAFADZOCHELSEAMUDA
"""
#label = lb
#entry = est
import tkinter as tk 

window = tk.Tk()
window.title('Student Registrat System')

stid = tk.Label(window)
stid.pack()

estname = tk.Entry(window)
estname.pack()

stname = tk.Label(window)
stname.pack()

estid = tk.Entry(window)
estid.pack()

stemail = tk.Label(window)
stemail.pack()

estemail = tk.Entry(window)
estemail.pack()

window.mainloop()