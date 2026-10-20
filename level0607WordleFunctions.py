# Work of Spencer Kemp

import random

secret_list = ["TRUCK", "TRAIN", "HALTS", "SKATE"]

words_already_guessed = []

attempt_display = 1

def choose_word():
    global secret_list
    global secret_word
    secret_word = random.choice(secret_list)
    #print(f"The computer chose {secret_word}.")

# Checks if the players guess is five letters long
def get_guess():
    global valid_word
    global player_guess
    global attempt_display
    valid_word = False
    print("\n"f"Attempt {attempt_display} of 6")
    player_guess = input("Enter a five-letter word: ").upper()
    if len(player_guess) == 5 and player_guess.isalpha() and player_guess not in words_already_guessed:
        valid_word = True
        attempt_display += 1
        words_already_guessed.append(player_guess) 
    else:
        print("not valid or already guessed. Try again.")
        get_guess()

# if guess is valid then run this
def evaluate_guess():
    global feedback_list
    feedback_list = []
    index_counter = -1
    for i in player_guess:
        index_counter += 1
        if i == secret_word[index_counter]:
            feedback_list.insert(index_counter, "G")
        elif i in secret_word: # why would in not think the last T in tarut is in train
            feedback_list.insert(index_counter, "Y")
        elif i not in secret_word:
            feedback_list.insert(index_counter, "-")

def display_guess():
    print("\n"f"Guess: {player_guess}")
    combined = " ".join(feedback_list)
    print(f"Feedback: {combined}")

def has_won():
    global attempt_display
    global words_already_guessed
    if player_guess == secret_word:
        print("\n""Congratulations! You solved the puzzle!")
    elif attempt_display > 6:
        print("\n"f"You used all 6 of your attempts. The secret word was {secret_word}.")
    if player_guess == secret_word or attempt_display > 6:
        play_again = input("Would you like to play again: ").lower()
        if play_again == "yes":
            attempt_display = 1
            words_already_guessed = []
            choose_word()
            return True
        else:
            print("Thanks for playing!")
            exit()
            return False
            