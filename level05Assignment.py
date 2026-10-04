# Work of Spencer Kemp

import random


computer_list = ["rock", "paper", "scissors"]

# checks if the player inputs a valid option against the computer
turns_used = 0
def get_player_choice():
    global turns_used
    global computer_list
    global player_choice
    global computer_choice
    player_choice = input("\n""Enter rock, paper, scissors: ").lower()
    if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
        turns_used += 1
        computer_choice = random.choice(computer_list)
        print(f"The computer chose {computer_choice}.")
        return True         
    else:
        print("\n"f"Sorry, {player_choice} is not a valid choice. Please try again.")
        return False


player_wins = 0
computer_wins = 0

def determine_winner(player_say, computer_say):
    global turns_used
    global player_wins
    global computer_wins
    # tie condition
    if player_say == computer_say:
        turns_used -= 1
        print("Tie! Play again.")
    # not tie condition
    elif player_say == "rock":
        if computer_say == "scissors":
            player_wins += 1
            print("You won!")
        else:
            computer_wins += 1
            print("You lost!")
    elif player_say == "paper":
        if computer_say == "rock":
            player_wins += 1
            print("You won!")
        else:
            computer_wins += 1
            print("You lost!")
    elif player_say == "scissors":
        if computer_say == "paper":
            player_wins += 1
            print("You won!")
        else:
            computer_wins += 1
            print("You lost!")
    

print("Welcome to Rock Paper Scissors!")
times_played = int(input("How many rounds would you like to play: "))

is_valid = False
# checking if they entered a valid number of rounds
while is_valid == False:
    if times_played % 2 != 0 and times_played > 0:
        is_valid = True
    else:
        times_played = int(input("\n""Sorry, the number must be a positive odd number. Please try again: "))
        continue

# runs the amount of times that the player chose
while turns_used < times_played:
    valid_choice = get_player_choice()
    if valid_choice == True:
        determine_winner(player_choice, computer_choice)

# score summary at the end of the game
print("\n""-------------------------")
print(f"Score — You: {player_wins} | Computer: {computer_wins}")
if player_wins > computer_wins:
    print("You won!!")
else:
    print("You lost!")
print("Thanks for playing!")