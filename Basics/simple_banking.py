# Simple Banking System

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"


# Example usage:
account = BankAccount("Ali", 1000)
print(account)
account.deposit(500)
account.withdraw(300)
print(account)
