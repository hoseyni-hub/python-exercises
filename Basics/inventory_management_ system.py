# Inventory Management System

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount

    def remove_stock(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Not enough stock to remove.")

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_inventory(self):
        for item in self.items:
            print(item)


# Example usage:
item1 = Item("Laptop", 10)
item2 = Item("Phone", 5)

inventory = Inventory()
inventory.add_item(item1)
inventory.add_item(item2)

inventory.show_inventory()
item1.remove_stock(2)
inventory.show_inventory()
