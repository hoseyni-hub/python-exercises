# week6_exercise6_sum_of_digits.py
# This program calculates the sum of digits of a number

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Example
number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))