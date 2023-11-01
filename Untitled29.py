#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import datetime

def add_expense(expense_list):
    expense_date = input("Enter expense date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(expense_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter again.")
        return

    expense_category = input("Enter expense category: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_list.append({"Date": expense_date, "Category": expense_category, "Amount": expense_amount})
    print("Expense added successfully!")

def generate_report(expense_list, month, year):
    report = [expense for expense in expense_list if expense["Date"].split("-")[1] == month and expense["Date"].split("-")[0] == year]

    if not report:
        print("No expenses found for the given month and year.")
        return
    
    total_expenses = sum([expense["Amount"] for expense in report])

    print("\nExpense Report - {}/{}:".format(month, year))
    print("========================")
    
    for expense in report:
        print("Date: {}, Category: {}, Amount: ${}".format(expense["Date"], expense["Category"], expense["Amount"]))

    print("========================")
    print("Total expenses: ${}".format(total_expenses))

def save_expenses(expense_list):
    file_name = input("Enter file name to save expenses: ")
    
    try:
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Date", "Category", "Amount"])
            writer.writeheader()
            writer.writerows(expense_list)
        print("Expenses saved successfully!")
    except IOError:
        print("An error occurred while saving the expenses.")

def load_expenses():
    file_name = input("Enter file name to load expenses: ")
    expense_list = []
    
    try:
        with open(file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            expense_list = [expense for expense in reader]
        print("Expenses loaded successfully!")
    except IOError:
        print("An error occurred while loading the expenses.")

    return expense_list

def main():
    expense_list = []
    
    while True:
        print("\nPersonal Expense Tracker")
        print("========================")
        print("1. Add Expense")
        print("2. Generate Monthly Report")
        print("3. Save Expenses")
        print("4. Load Expenses")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_expense(expense_list)
        elif choice == '2':
            month = input("Enter month (MM): ")
            year = input("Enter year (YYYY): ")
            generate_report(expense_list, month, year)
        elif choice == '3':
            save_expenses(expense_list)
        elif choice == '4':
            expense_list = load_expenses()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




