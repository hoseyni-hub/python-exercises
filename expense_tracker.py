# Expense Tracker

expenses = {}

while True:
    print("\n💰 Expense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Total spent")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category (Food, Rent, Transport, etc.): ")
        amount = float(input("Enter amount: "))
        expenses[category] = expenses.get(category, 0) + amount
        print("✅ Expense added!")
    elif choice == "2":
        print("\nExpenses by category:")
        for cat, amt in expenses.items():
            print(f"{cat}: {amt} $")
    elif choice == "3":
        total = sum(expenses.values())
        print(f"\nTotal spent: {total} $")
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")