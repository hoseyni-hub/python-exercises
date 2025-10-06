# Function using *args
def add_numbers(*args):
    return sum(args)

# Function using **kwargs
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    print("Sum:", add_numbers(1, 2, 3, 4, 5))

    print("\nUser Info:")
    print_user_info(name="John", age=30, country="Canada")