import json

FILENAME = "contacts.json"

def load_contacts():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f)

contacts = load_contacts()

while True:
    print("\nOptions: add, show, quit")
    command = input("Enter command: ").lower()

    if command == "quit":
        save_contacts(contacts)
        break
    elif command == "add":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("Contact added.")
    elif command == "show":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Unknown command.")
