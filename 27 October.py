# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 08:49:09 2025

@author: ROPAFADZOCHELSEAMUDA
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Function to create the database and table
def createdb():
    try:
        conn = sqlite3.connect("richfield.db")
        cursor = conn.cursor()
        createtable = """
        CREATE TABLE IF NOT EXISTS st_Details (
            name VARCHAR(20) NOT NULL,
            tage INTEGER,
            email VARCHAR(25) PRIMARY KEY,
            grade CHAR(1)
        )
        """
        cursor.execute(createtable)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")

def addrecord():
    createdb()
    conn = sqlite3.connect("richfield.db")
    cursor = conn.cursor()

    name = ename.get()
    if not name:
        messagebox.showerror("Error", "Name is required!")
        return

    try:
        age = int(eage.get())
    except ValueError:
        messagebox.showerror("Incorrect Value", "Enter an integer for age")
        return

    email = eemail.get()
    if not email:
        messagebox.showerror("Error", "Email is required!")
        return
    grade = egrade.get()
    if not grade:
        messagebox.showerror("Error", "Grade is required!")
        return

    try:
        cursor.execute("INSERT INTO st_Details (name, tage, email, grade) VALUES (?, ?, ?, ?)",
                       (name, age, email, grade))
        conn.commit()
        messagebox.showinfo("Success", "Record added successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists!")
    finally:
        conn.close()

def viewall():
    coon = None
    try:
        
        conn = sqlite3.connect("richfield2.db")
        cursor = conn.cursor()

    for item in treedis.get_children():
        treedis.delete(item)

    cursor.execute("SELECT * FROM st_Details")
    rows = cursor.fetchall()
        
    for row in rows:
        treedis.insert('', tk.END, values=row)

    conn.close()

# GUI setup
root = tk.Tk()
root.title("Student Management System")

# Labels and Entry Fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
ename = tk.Entry(root, borderwidth=3, bg='lightgreen')
ename.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
eage = tk.Entry(root, borderwidth=3, bg='lightgreen')
eage.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
eemail = tk.Entry(root, borderwidth=3, bg='lightgreen')
eemail.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Grade:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
egrade = tk.Entry(root, borderwidth=3, bg='lightgreen')
egrade.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Student", bg='green', fg='white', command=addrecord).grid(row=4, column=0, padx=10, pady=20)
tk.Button(root, text="View All", bg='blue', fg='white', command=viewall).grid(row=4, column=1, padx=10, pady=20)
tk.Button(root, text="Search", bg='lightblue', fg='brown').grid(row=4, column=2, padx=10, pady=20)
tk.Button(root, text="Update", bg='yellow').grid(row=4, column=3, padx=10, pady=20)
tk.Button(root, text="Delete", bg='red', fg='white').grid(row=4, column=4, padx=10, pady=20)

# Treeview to display records
treedis = ttk.Treeview(root, columns=("Name", "Age", "Email", "Grade"), show='headings', height=8)
treedis.grid(row=5, column=0, columnspan=5, padx=10, pady=10)

# Define headings
for col in ("Name", "Age", "Email", "Grade"):
    treedis.heading(col, text=col)

root.mainloop()