# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
root = Tk()
root.geometry('400x150')

def action():
    word = entryWord.get()
    reversed_word = word[::-1]
    lblResult['text'] = reversed_word

# Create Label and entry word 
lblWord = Label(root, text='Enter a word:')
lblWord.place(x=20, y=20)
entryWord = Entry(root)
entryWord.place(x=150, y=20, width=225, height=25)

# Create label to display result
lblResult = Label(root, text="result.....")
lblResult.place(x=150, y=60)

# Create a button to perform action
btnAction = Button(root, text="Validate", command=action)
btnAction.place(x=150, y=100, width=225, height=30)

root.mainloop()

