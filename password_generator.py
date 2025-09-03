import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

while True:
    try:
        length = int(input("Enter password length (0 to quit): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if length == 0:
        break
    print("Generated password:", generate_password(length))