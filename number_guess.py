import random

number = random.randint(1, 100)
print("Guess the number between 1 and 100!")

while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed it!")
        break