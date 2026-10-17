# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 13:49:25 2025

@author: ROPAFADZOCHELSEAMUDA
"""

# -*- coding: utf-8 -*-
  
"""
Library Borrowing App implementing:
- books table (id, title, quantity)
- borrowed_books (id, student_name, book_id, borrow_date, return_date, fine)
Features:
- Borrow form (Student name, Book combobox filtered by quantity > 0,
  DateEntry for borrow & return, validation)
- Add/Delete/Clear buttons (Add decreases quantity, Delete increases quantity)
- Fine calculation: R5 per day overdue
- Borrowed books Treeview with real-time search and record count
- Highlight rows with fine > 0 in red; blue header with bold white font
"""

import sqlite3

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
from tkcalendar import DateEntry

# ---------------- DATABASE SETUP ---------------- #
connector = sqlite3.connect('library.db')
cursor = connector.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    quantity INTEGER NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS borrowed_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    book_id INTEGER,
    borrow_date TEXT,
    return_date TEXT,
    fine REAL DEFAULT 0,
    FOREIGN KEY(book_id) REFERENCES books(id)
)''')

# Sample data insertion if empty
cursor.execute("SELECT COUNT(*) FROM books")
if cursor.fetchone()[0] == 0:
    books_data = [
        ("Learn Python", 3),
        ("Database Systems", 2),
        ("Web Development", 1),
        ("Networking Basics", 2),
        ("Computer networks ", 1)
    ]
    cursor.executemany("INSERT INTO books (title, quantity) VALUES (?, ?)", books_data)
    connector.commit()

# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("Student Book - Index")
root.geometry("900x550")
root.configure(bg='lightgray')

# ---------------- FUNCTIONS ---------------- #
def calculate_fine(return_date_str):
    """Calculates fine based on today's date and return date."""
    today = date.today()
    return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
    diff = (today - return_date).days
    return 5 * diff if diff > 0 else 0

def format_date_display(db_date_str):
    """Convert YYYY-MM-DD to MM/DD/YY format for display"""
    if db_date_str:
        db_date = datetime.strptime(db_date_str, "%Y-%m-%d")
        return db_date.strftime("%m/%d/%y")
    return ""

def format_date_storage(display_date_str):
    """Convert MM/DD/YY to YYYY-MM-DD format for storage"""
    if display_date_str:
        display_date = datetime.strptime(display_date_str, "%m/%d/%y")
        return display_date.strftime("%Y-%m-%d")
    return ""

def refresh_table():
    """Refreshes data displayed in the table."""
    for row in table.get_children():
        table.delete(row)

    cursor.execute('''SELECT borrowed_books.id, student_name, title, borrow_date, return_date, fine
                      FROM borrowed_books
                      JOIN books ON borrowed_books.book_id = books.id''')
    records = cursor.fetchall()

    # Update fines dynamically in case return date passed
    for rec in records:
        rec_id, student, title, borrow_date, return_date, fine = rec
        new_fine = calculate_fine(return_date)
        if new_fine != fine:
            cursor.execute("UPDATE borrowed_books SET fine=? WHERE id=?", (new_fine, rec_id))
            connector.commit()
        
        # Format dates for display
        display_borrow = format_date_display(borrow_date)
        display_return = format_date_display(return_date)
        
        tag = 'fine' if new_fine > 0 else ''
        table.insert('', 'end', values=(rec_id, student, title, display_borrow, display_return, new_fine), tags=(tag,))

    total_label.config(text=f"Total Borrowed Books: {len(records)}")
    load_books()

def load_books():
    """Loads available books into combobox."""
    cursor.execute("SELECT title FROM books WHERE quantity > 0")
    books = [b[0] for b in cursor.fetchall()]
    book_combo['values'] = books

def add_record():
    """Adds a borrowed book record."""
    student = student_entry.get().strip()
    book_title = book_combo.get()
    
    # Get dates from calendar widgets
    b_date = borrow_entry.get_date()
    r_date = return_entry.get_date()

    if not student or not book_title:
        messagebox.showerror("Error", "All fields are required")
        return

    if b_date < date.today():
        messagebox.showerror("Error", "Borrow date cannot be in the past.")
        return
    if r_date < b_date:
        messagebox.showerror("Error", "Return date cannot be before borrow date.")
        return

    cursor.execute("SELECT id, quantity FROM books WHERE title=?", (book_title,))
    book = cursor.fetchone()

    # FIXED: Check if book exists and has quantity > 0
    if book is None:
        messagebox.showerror("Error", "Book not found in database")
        return
        
    if book[1] > 0:
        fine = calculate_fine(r_date.strftime("%Y-%m-%d"))
        cursor.execute('''INSERT INTO borrowed_books (student_name, book_id, borrow_date, return_date, fine)
                          VALUES (?, ?, ?, ?, ?)''',
                       (student, book[0], b_date.strftime("%Y-%m-%d"), r_date.strftime("%Y-%m-%d"), fine))
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE id=?", (book[0],))
        connector.commit()
        messagebox.showinfo("Success", "Book borrowed successfully!")
        clear_fields()
        refresh_table()
    else:
        messagebox.showerror("Error", "Book not available")

def delete_record():
    """Deletes a selected record."""
    selected = table.selection()
    if not selected:
        messagebox.showerror("Error", "Select a record to delete")
        return

    rec_id = table.item(selected[0])['values'][0]
    book_title = table.item(selected[0])['values'][2]

    confirm = messagebox.askyesno("Confirm", f"Delete record for '{book_title}'?")
    if confirm:
        cursor.execute("SELECT id FROM books WHERE title=?", (book_title,))
        book_result = cursor.fetchone()
        
        # FIXED: Check if book exists before proceeding
        if book_result is None:
            messagebox.showerror("Error", "Book not found in database")
            return
            
        book_id = book_result[0]
        cursor.execute("DELETE FROM borrowed_books WHERE id=?", (rec_id,))
        cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE id=?", (book_id,))
        connector.commit()
        refresh_table()
        messagebox.showinfo("Deleted", "Record deleted successfully.")

def clear_fields():
    """Clears form fields."""
    student_entry.delete(0, 'end')
    book_combo.set('')
    borrow_entry.set_date(date.today())
    return_entry.set_date(date.today())

def search_records(event=None):
    """Searches for student or book records."""
    query = search_var.get().lower()
    for row in table.get_children():
        table.delete(row)

    cursor.execute('''SELECT borrowed_books.id, student_name, title, borrow_date, return_date, fine
                      FROM borrowed_books
                      JOIN books ON borrowed_books.book_id = books.id
                      WHERE LOWER(student_name) LIKE ? OR LOWER(title) LIKE ?''',
                   (f'%{query}%', f'%{query}%'))
    results = cursor.fetchall()

    for rec in results:
        rec_id, student, title, borrow_date, return_date, fine = rec
        display_borrow = format_date_display(borrow_date)
        display_return = format_date_display(return_date)
        tag = 'fine' if fine > 0 else ''
        table.insert('', 'end', values=(rec_id, student, title, display_borrow, display_return, fine), tags=(tag,))
    
    total_label.config(text=f"Total Borrowed Books: {len(results)}")

# ---------------- HEADER ---------------- #
header_frame = tk.Frame(root, bg='lightgray')
header_frame.pack(fill='x', padx=10, pady=5)

tk.Label(header_frame, text="Student Book - Index", font=('Arial', 16, 'bold'), 
         bg='lightgray').pack()

# ---------------- SOURCE SECTION ---------------- #
source_frame = tk.LabelFrame(root, text="Source: Book", font=('Arial', 10, 'bold'), bg='lightgray')
source_frame.pack(fill='x', padx=10, pady=5)

# Student Name and Book in one row
name_book_frame = tk.Frame(source_frame, bg='lightgray')
name_book_frame.pack(fill='x', pady=2)

tk.Label(name_book_frame, text="Student Name:", bg='lightgray').pack(side='left', padx=5)
student_entry = tk.Entry(name_book_frame, width=20)
student_entry.pack(side='left', padx=5)

tk.Label(name_book_frame, text="Book:", bg='lightgray').pack(side='left', padx=5)
book_combo = ttk.Combobox(name_book_frame, state='readonly', width=20)
book_combo.pack(side='left', padx=5)

# Dates in another row
date_frame = tk.Frame(source_frame, bg='lightgray')
date_frame.pack(fill='x', pady=2)

tk.Label(date_frame, text="Source Date:", bg='lightgray').pack(side='left', padx=5)
borrow_entry = DateEntry(date_frame, width=12, background='darkblue',
                        foreground='white', borderwidth=2, date_pattern='mm/dd/y')
borrow_entry.pack(side='left', padx=5)

tk.Label(date_frame, text="Return Date:", bg='lightgray').pack(side='left', padx=5)
return_entry = DateEntry(date_frame, width=12, background='darkblue',
                        foreground='white', borderwidth=2, date_pattern='mm/dd/y')
return_entry.pack(side='left', padx=5)

# ---------------- BUTTONS ---------------- #
button_frame = tk.Frame(root, bg='lightgray')
button_frame.pack(fill='x', padx=10, pady=10)

tk.Button(button_frame, text="Add", bg="green", fg="white", command=add_record, 
          width=10).pack(side='left', padx=5)
tk.Button(button_frame, text="Delete", bg="red", fg="white", command=delete_record,
          width=10).pack(side='left', padx=5)
tk.Button(button_frame, text="Clear", bg="gray", fg="white", command=clear_fields,
          width=10).pack(side='left', padx=5)

# Separator
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=10, pady=5)

# ---------------- SEARCH ---------------- #
search_frame = tk.Frame(root, bg='lightgray')
search_frame.pack(fill='x', padx=10, pady=5)

tk.Label(search_frame, text="Search:", bg='lightgray').pack(side='left')
search_var = tk.StringVar()
search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
search_entry.pack(side='left', padx=5)
search_entry.bind('<KeyRelease>', search_records)

# ---------------- TABLE ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(fill='both', expand=True, padx=10, pady=5)

columns = ('ID', 'Students', 'Book', 'Barrow Date', 'Return Date', 'Time')
table = ttk.Treeview(table_frame, columns=columns, show='headings', height=8)

# Configure columns
table.column('ID', width=50, anchor='center')
table.column('Students', width=150, anchor='w')
table.column('Book', width=150, anchor='w')
table.column('Barrow Date', width=100, anchor='center')
table.column('Return Date', width=100, anchor='center')
table.column('Time', width=80, anchor='center')

for col in columns:
    table.heading(col, text=col)

table.tag_configure('fine', background='salmon')

scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
table.pack(fill='both', expand=True)

# ---------------- TOTAL LABEL ---------------- #
total_frame = tk.Frame(root, bg='lightgray')
total_frame.pack(fill='x', padx=10, pady=5)

total_label = tk.Label(total_frame, text="Total Borrowed Books: 0", font=('Arial', 10, 'bold'), 
                       bg='lightgray')
total_label.pack()

# ---------------- SAMPLE DATA FUNCTION ---------------- #
def add_sample_data():
    """Add sample data if no records exist"""
    cursor.execute("SELECT COUNT(*) FROM borrowed_books")
    if cursor.fetchone()[0] == 0:
        # Add sample borrowed records
        sample_records = [
            ("Alice Johnson", "Learn Python", "2025-06-01", "2025-06-10", 0.0),
            ("Bob Smith", "Database Systems", "2025-06-05", "2025-06-12", 0.0)
        ]
        
        for student, book_title, borrow_date, return_date, fine in sample_records:
            cursor.execute("SELECT id FROM books WHERE title=?", (book_title,))
            book_result = cursor.fetchone()
            
            # FIXED: Check if book exists before inserting
            if book_result is not None:
                book_id = book_result[0]
                cursor.execute('''INSERT INTO borrowed_books (student_name, book_id, borrow_date, return_date, fine)
                                VALUES (?, ?, ?, ?, ?)''',
                             (student, book_id, borrow_date, return_date, fine))
                cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE id=?", (book_id,))
        
        connector.commit()

# ---------------- RUN ---------------- #
add_sample_data()
refresh_table()
root.mainloop()

# Close database connection when app closes
connector.close()