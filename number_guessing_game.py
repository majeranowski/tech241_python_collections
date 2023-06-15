"""
Make a magic number game using Python.

The game should:

set a number as the answer

ask the user for a guess

check if the user’s guess was correct

if it was, congratulate them. If not give them another guess (up to 3 guesses)

Here is some extremely basic Pseudocode to get you started (I recommend researching and using pseudocode often as it is very helpful):

# Magic number game

# Set magic number

# Ask the user for a guess

# Check if the user's guess was correct

# Give them the result

Okay if you did that, I want some new features. Give these a try!



Can you make the generated number random (not coded by yourself)?

Can you give the user feedback if their number was too high or too low?

Can you make sure the user enters an int?

Can you let the user start a new game, with a new number, if they do not win with their 3 guesses?

Can you make the game quittable before the end (without stopping it in Python)?
"""

import random

def play_game():
    answer = random.randint(1, 10)  # Generate a random number between 1 and 10
    counter = 0

    while counter < 3:

        guess = int(input("Guess the magic number (between 1 and 100) or quit by pressing 0: "))


        if guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")

        else:
            print("Congratulations! You guessed the magic number!")
            return

        counter += 1

    print("Out of guesses. The magic number was", answer)

play_game()

wanna_play = True
while wanna_play:
    choice = input("Do you want to play again? (y/n): ")
    if choice.lower() == "y":
        play_game()
    else:
        print("Thank you for playing the Magic Number game!")
        wanna_play = False
