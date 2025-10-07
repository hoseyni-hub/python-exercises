# Number Comparison
# This program compares two numbers and prints the larger one.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print(f"The larger number is: {a}")
elif b > a:
    print(f"The larger number is: {b}")
else:
    print("Both numbers are equal.")
