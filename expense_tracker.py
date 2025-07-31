import json
import os

filename = "expense.json"

# Load existing expenses or start a new list
if os.path.exists(filename):
    with open(filename, "r") as file:
        try:
            expenses = json.load(file)
        except json.decoder.JSONDecodeError:
            expenses = []
else:
    expenses = []

def save_expenses():
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    item = input("Enter expense item: ")
    try:
        amount = float(input("Enter amount: "))
        expenses.append({"item": item, "amount": amount})
        save_expenses()
        print("✅ Expense saved successfully!\n")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.\n")

def view_expenses():
    if not expenses:
        print("📭 No expenses recorded yet.\n")
        return

    print("\n📋 Your Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['item']} - Ksh {exp['amount']}")
    
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spent: Ksh {total}\n")

# Main menu loop
while True:
    print("=== Expense Tracker Menu ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.\n")
