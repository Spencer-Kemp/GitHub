# Work of Spencer Kemp

import random
from level0607WordleFunctions import (
choose_word,
get_guess,
evaluate_guess,
display_guess,
has_won
)


num_of_attempts = 1

# The welcome statment and instructions
print("Welcome to Mystery Wordle!")
print("\n""Guess the five-letter word. You have up to 6 guesses.")
print("\n""G = correct letter and position")
print("Y = correct letter, wrong position")
print("- = letter is not in the word")

choose_word()

while num_of_attempts < 7:
    get_guess()
    if get_guess:
        num_of_attempts += 1
        evaluate_guess()
        display_guess()
        has_won()
        if has_won:
            num_of_attempts = 1
            