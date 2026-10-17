# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 08:44:59 2025

@author: ROPAFADZOCHELSEAMUDA
"""
import tkinter as tk
from tkinter import messagebox

# Function to display entered information
def submit_form():
    name = name_entry.get()
    student_id = id_entry.get()
    email = email_entry.get()

    # Collect selected courses
    selected_courses = []
    if var1.get():
        selected_courses.append("Python Programming")
    if var2.get():
        selected_courses.append("Data Structures")
    if var3.get():
        selected_courses.append("Web Development")
    if var4.get():
        selected_courses.append("Database Management")

    # Check if required fields are filled
    if not name or not student_id or not email:
        messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
        return

    # Format and display message
    courses = ", ".join(selected_courses) if selected_courses else "None"
    info = (
        f"Registration Successful!\n\n"
        f"Name: {name}\n"
        f"Student ID: {student_id}\n"
        f"Email: {email}\n"
        f"Courses Selected: {courses}"
    )
    messagebox.showinfo("Registration Details", info)

# Function to clear all fields
def clear_form():
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)

# Create main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x400")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Student Registration Form", font=("Arial", 16, "bold")).pack(pady=10)

# Frame for form fields
frame = tk.Frame(root)
frame.pack(pady=10)

# Labels and Entries
tk.Label(frame, text="Student Name:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Student ID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
id_entry = tk.Entry(frame, width=30)
id_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Email Address:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1, pady=5)

# Courses Section
tk.Label(root, text="Select Courses:", font=("Arial", 12, "bold")).pack(anchor="w", padx=40)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

tk.Checkbutton(root, text="Python Programming", variable=var1).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Data Structures", variable=var2).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Web Development", variable=var3).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Database Management", variable=var4).pack(anchor="w", padx=60)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Submit", width=12, bg="green", fg="white", command=submit_form).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Clear", width=12, bg="red", fg="white", command=clear_form).grid(row=0, column=1, padx=10)

# Run the main loop
root.mainloop()
 

