# Simple Calculator
# This program performs basic arithmetic operations.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Choose operation: + - * /")
op = input("Operation: ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operation.")