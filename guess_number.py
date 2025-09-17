import random

print("🎲 Guess the Number Game!")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < number:
        print("Too low! ⬇️")
    elif guess > number:
        print("Too high! ⬆️")
    else:
        print(f"🎉 Correct! The number was {number}. Attempts: {attempts}")
        break