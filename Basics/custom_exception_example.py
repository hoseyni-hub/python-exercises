class NegativeNumberError(Exception):
    """Custom exception for handling negative numbers."""
    pass

def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number.")
    return number ** 0.5

if __name__ == "__main__":
    try:
        print(calculate_square_root(16))
        print(calculate_square_root(-9))
    except NegativeNumberError as e:
        print("Custom Error Caught:", e)