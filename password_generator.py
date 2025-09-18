import random
import string

print("🔑 Password Generator")

length = int(input("Enter password length: "))

chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))

print(f"Your generated password: {password}")