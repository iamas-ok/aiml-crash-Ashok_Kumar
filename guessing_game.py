# Build number guassing game

import random

def play_guessing_game():
    secret = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it?\n")

    while True:
        # --- Get valid input ---
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.\n")
            continue

        attempts += 1

        # --- Give feedback ---
        if guess < secret:
            print(f"low, Try higher.\n")
        elif guess > secret:
            print(f"high, Try lower.\n")
        else:
            print(f" Correct, The number was {secret}.")
            print(f" You got it in {attempts} attempt{'s' if attempts != 1 else ''}!")
            break

play_guessing_game()