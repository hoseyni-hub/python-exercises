def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Simple Calculator")
print("Operations: add, subtract, multiply, divide")

while True:
    op = input("\nEnter operation (or 'quit' to exit): ").lower()
    if op == "quit":
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    if op == "add":
        print("Result:", add(num1, num2))
    elif op == "subtract":
        print("Result:", subtract(num1, num2))
    elif op == "multiply":
        print("Result:", multiply(num1, num2))
    elif op == "divide":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation.")