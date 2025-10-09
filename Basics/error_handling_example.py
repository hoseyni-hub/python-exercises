def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(5, 0))