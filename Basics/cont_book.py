# Contact Book

contacts = {}

while True:
    print("\n📖 Contact Book")
    print("1. Add contact")
    print("2. Search contact")
    print("3. View all contacts")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("✅ Contact saved!")
    elif choice == "2":
        name = input("Enter name to search: ")
        print(f"{name}: {contacts.get(name, 'Not found')}")
    elif choice == "3":
        print("\nAll contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
