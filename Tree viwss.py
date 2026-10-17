# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 10:18:19 2025

@author: ROPAFADZOCHELSEAMUDA
"""


import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime, date

# ---------- Database Setup ---------- #
db = sqlite3.connect("library.db")
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS borrowed_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    book_id INTEGER NOT NULL,
    borrow_date TEXT NOT NULL,
    return_date TEXT NOT NULL,
    fine REAL DEFAULT 0,
    FOREIGN KEY (book_id) REFERENCES books(id)
)
""")

# ---------- Helper Functions ---------- #
def get_books():
    cur.execute("SELECT id, title FROM books WHERE quantity > 0")
    return cur.fetchall()

def calculate_fine(ret_date):
    days = (date.today() - datetime.strptime(ret_date, "%m/%d/%y").date()).days
    return max(0, days * 1)  # R1 per overdue day

# ---------- Main App ---------- #
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("900x500")

        # --- Form Section --- #
        frame = LabelFrame(root, text="Borrow Book", padx=10, pady=10)
        frame.pack(fill="x", padx=20, pady=10)

        Label(frame, text="Student Name").grid(row=0, column=0)
        self.name_entry = Entry(frame, width=25)
        self.name_entry.grid(row=0, column=1, padx=5)

        Label(frame, text="Book").grid(row=0, column=2)
        self.book_combo = ttk.Combobox(frame, width=25, state="readonly")
        self.refresh_books()
        self.book_combo.grid(row=0, column=3, padx=5)

        Label(frame, text="Borrow Date").grid(row=1, column=0)
        self.borrow_date = DateEntry(frame, width=18)
        self.borrow_date.grid(row=1, column=1, padx=5)

        Label(frame, text="Return Date").grid(row=1, column=2)
        self.return_date = DateEntry(frame, width=18)
        self.return_date.grid(row=1, column=3, padx=5)

        Button(frame, text="Borrow", command=self.borrow_book, bg="#4CAF50", fg="white").grid(row=2, column=0, pady=5)
        Button(frame, text="Delete", command=self.delete_record, bg="#F44336", fg="white").grid(row=2, column=1)
        Button(frame, text="Refresh", command=self.show_records).grid(row=2, column=2)

        # --- Borrowed Books Table --- #
        cols = ("ID", "Student", "Book", "Borrow Date", "Return Date", "Fine")
        self.tree = ttk.Treeview(root, columns=cols, show="headings", height=15)
        for c in cols: self.tree.heading(c, text=c)
        self.tree.pack(fill=BOTH, expand=True, padx=20, pady=10)

        self.show_records()

    # ---------- Functions ---------- #
    def refresh_books(self):
        books = [b[1] for b in get_books()]
        self.book_combo["values"] = books

    def borrow_book(self):
        name = self.name_entry.get().strip()
        book = self.book_combo.get()
        borrow_date = self.borrow_date.get()
        return_date = self.return_date.get()

        if not name or not book:
            messagebox.showerror("Error", "Please enter all details.")
            return

        cur.execute("SELECT id, quantity FROM books WHERE title=?", (book,))
        book_data = cur.fetchone()
        if not book_data or book_data[1] <= 0:
            messagebox.showerror("Error", "Book not available.")
            return

        fine = calculate_fine(return_date)
        cur.execute("INSERT INTO borrowed_books (student_name, book_id, borrow_date, return_date, fine) VALUES (?,?,?,?,?)",
                    (name, book_data[0], borrow_date, return_date, fine))
        cur.execute("UPDATE books SET quantity=quantity-1 WHERE id=?", (book_data[0],))
        db.commit()
        self.show_records()
        self.refresh_books()
        messagebox.showinfo("Success", f"{book} borrowed successfully!")

    def show_records(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        cur.execute("""
            SELECT b.id, b.student_name, bk.title, b.borrow_date, b.return_date, b.fine
            FROM borrowed_books b
            JOIN books bk ON b.book_id = bk.id
            ORDER BY b.id DESC
        """)
        for row in cur.fetchall():
            self.tree.insert("", END, values=row)

    def delete_record(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a record to delete.")
            return
        borrow_id = self.tree.item(selected[0])["values"][0]
        cur.execute("SELECT book_id FROM borrowed_books WHERE id=?", (borrow_id,))
        book_id = cur.fetchone()[0]
        cur.execute("DELETE FROM borrowed_books WHERE id=?", (borrow_id,))
        cur.execute("UPDATE books SET quantity=quantity+1 WHERE id=?", (book_id,))
        db.commit()
        self.show_records()
        self.refresh_books()

# ---------- Run App ---------- #
root = Tk()
app = LibraryApp(root)
root.mainloop()
