# Task: Create a simple "Guess the number" game with a loop.

import random

def guess_game():
    number = random.randint(1, 20)
    attempts = 0

    print("Guess the number between 1 and 20!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You found the number in {attempts} attempts.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guess_game()