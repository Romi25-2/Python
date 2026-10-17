2.00# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 12:10:53 2025

@author: ROPAFADZOCHELSEAMUDA
"""

import os
import csv

invent_file = "inventory.txt"
field_names = ['ID', 'Name', 'Category', 'Quantity', 'Price']


def initialize_inventory():
    if not os.path.exists(invent_file):
        sample_data = [
            {'ID': '1', 'Name': 'Apple', 'Category': 'Fruits', 'Quantity': '50', 'Price': '0.50'},
            {'ID': '2', 'Name': 'Banana', 'Category': 'Fruits', 'Quantity': '30', 'Price': '0.30'},
            {'ID': '3', 'Name': 'Milk', 'Category': 'Dairy', 'Quantity': '20', 'Price': '1.20'},
            {'ID': '4', 'Name': 'Bread', 'Category': 'Bakery', 'Quantity': '15', 'Price': '2.00'},
        ]
        with open(invent_file, mode='w', newline='') as f:
            writer = csv.DictWriter(f, field_names=field_names)
            writer.writeheader()
            writer.writerows(sample_data)


def load_inventory():
    with open(invent_file, mode='r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_inventory(inventory):
    with open(invent_file, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(inventory)


def add_product():
    inventory = load_inventory()
    new_product = {
        'ID': input("Enter product ID: "),
        'Name': input("Enter product name: "),
        'Category': input("Enter product category: "),
        'Quantity': input("Enter quantity: "),
        'Price': input("Enter price: ")
    }
    inventory.append(new_product)
    save_inventory(inventory)
    print("Product added successfully!")


def update_product():
    inventory = load_inventory()
    product_id = input("Enter product ID to update: ")
    for product in inventory:
        if product['ID'] == product_id:
            product['Name'] = input(f"Enter new name [{product['Name']}]: ") or product['Name']
            product['Category'] = input(f"Enter new category [{product['Category']}]: ") or product['Category']
            product['Quantity'] = input(f"Enter new quantity [{product['Quantity']}]: ") or product['Quantity']
            product['Price'] = input(f"Enter new price [{product['Price']}]: ") or product['Price']
            save_inventory(inventory)
            print("Product updated successfully!")
            return
    print("Product ID not found.")


def delete_product():
    inventory = load_inventory()
    product_id = input("Enter product ID to delete: ")
    inventory = [p for p in inventory if p['ID'] != product_id]
    save_inventory(inventory)
    print("Product deleted successfully!")


def sort_by_price():
    inventory = load_inventory()
    sorted_inventory = sorted(inventory, key=lambda x: float(x['Price']))
    for product in sorted_inventory:
        print(product)


def filter_by_category():
    inventory = load_inventory()
    category = input("Enter category to filter: ")
    filtered = [p for p in inventory if p['Category'].lower() == category.lower()]
    for product in filtered:
        print(product)


def inventory_summary():
    inventory = load_inventory()
    print("\n--- Inventory Summary ---")
    for product in inventory:
        print(product)


def category_summary():
    inventory = load_inventory()
    summary = {}
    for product in inventory:
        category = product['Category']
        quantity = int(product['Quantity'])
        value = float(product['Price']) * quantity
        if category not in summary:
            summary[category] = {'count': 0, 'total_value': 0.0}
        summary[category]['count'] += quantity
        summary[category]['total_value'] += value
    print("\n--- Category Summary ---")
    for cat, data in summary.items():
        print(f"Category: {cat}, Total Items: {data['count']}, Total Value: ${data['total_value']:.2f}")


def display_menu():
    print("\nInventory Management System")
    print("1. Add New Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Sort Products by Price")
    print("5. Filter Products by Category")
    print("6. Inventory Summary")
    print("7. Category Summary")
    print("8. Exit")


def main():
    initialize_inventory()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            sort_by_price()
        elif choice == '5':
            filter_by_category()
        elif choice == '6':
            inventory_summary()
        elif choice == '7':
            category_summary()
        elif choice == '8':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

    