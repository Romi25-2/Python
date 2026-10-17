# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 14:45:31 2025

@author: ROPAFADZOCHELSEAMUDA
"""

import tkinter as tk

root = tk.Tk()

canv = tk.Canvas(root, width=520, height=600, bg="pink")
canv.pack()

# Corrected rectangle coordinates (x1, y1, x2, y2)
#canv.create_rectangle(100, 100, 120, 120)

canv.create_text(200, 175, text="hello peter")
canv.create_polygon(100,100,100,200,250,400,300,300,405,500, fill="red", )

canv.create_oval(200,100,300,450, fill="red")

root.mainloop()