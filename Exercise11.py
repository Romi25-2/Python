# -*- coding: utf-8 -*-
"""
Created on Thu May  8 12:30:45 2025

@author: ROPAFADZOCHELSEAMUDA
"""

import os

# Define the filename
FILENAME = 'bscit.txt'

# Sample data to initialize the file if it doesn't exist
SAMPLE_DATA = [
    "S101,Alice Johnson,Programming Fundamentals,85,90",
    "S102,Bob Smith,Data Structures,78,82",
    "S103,Charlie Lee,Algorithms,92,88"
]

def initialize_file():
    """Initialize the file with sample data if it doesn't exist."""
    with open(FILENAME, 'w') as file:
        for record in SAMPLE_DATA:
            file.write(record + '\n')

def load_records():
    """Load records from the file."""
    if not os.path.exists(FILENAME):
        initialize_file()
    
    with open(FILENAME, 'r') as file:
        records = [line.strip().split(',') for line in file.readlines()]
    return records

def save_records(records):
    """Save records to the file."""
    with open(FILENAME, 'w') as file:
        for record in records:
            file.write(','.join(record) + '\n')

def display_records(records):
    """Display all records."""
    print("\nID\tName\t\tModule\t\tTest Mark\tExam Mark")
    print("-" * 60)
    for record in records:
        print("\t".join(record))
    print("\n")

def add_record(records):
    """Add a new record."""
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    module = input("Enter Module: ")
    testmark = input("Enter Test Mark: ")
    exammark = input("Enter Exam Mark: ")
    
    records.append([student_id, name, module, testmark, exammark])
    save_records(records)
    print("Record added successfully!\n")

def update_record(records):
    """Update an existing record."""
    student_id = input("Enter Student ID to update: ")
    for record in records:
        if record[0] == student_id:
            print("Current Record: ", record)
            record[1] = input("Enter new Name: ")
            record[2] = input("Enter new Module: ")
            record[3] = input("Enter new Test Mark: ")
            record[4] = input("Enter new Exam Mark: ")
            save_records(records)
            print("Record updated successfully!\n")
            return
    print("Record not found!\n")

def main():
    """Main function to run the program."""
    records = load_records()
    
    while True:
        print("Menu:")
        print("1. Add a new record")
        print("2. Update an existing record")
        print("3. Display all marks details")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_record(records)
        elif choice == '2':
            update_record(records)
        elif choice == '3':
            display_records(records)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
