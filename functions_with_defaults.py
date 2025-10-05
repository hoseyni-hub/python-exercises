# A function with a default argument
def greet(name="Guest"):
    return f"Hello, {name}!"

# A function with multiple default arguments
def calculate_price(price, tax=0.1, discount=0.05):
    """
    Calculate final price after tax and discount.
    """
    taxed = price + (price * tax)
    final_price = taxed - (taxed * discount)
    return final_price

if __name__ == "__main__":
    print(greet())
    print(greet("Alice"))

    print("Price with defaults:", calculate_price(100))
    print("Price with custom tax/discount:", calculate_price(100, tax=0.2, discount=0.1))