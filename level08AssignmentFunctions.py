# work of Spencer Kemp
import random

class BankAccount:

    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00
        
    def display_options(self): # displays menu options and allows the user to pick
        global player_choice
        valid_choice = False
        print("\n""Please choose an option:""\n")
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. View account information")
        print("4. Quit""\n")
        while valid_choice == False:
            player_choice = input("")
            print("")
            if player_choice == "1" or player_choice == "2" or player_choice == "3" or player_choice =="4":
                player_choice = int(player_choice)
                valid_choice == True
                return
            else:
                print("Invalid choice. Please try again.")
            

    def deposit(self): 
        global deposit_amount
        if player_choice == 1:
            print("How much would you like to deposit?")
            deposit_amount = (input(""))
            try:
                deposit_amount = float(deposit_amount)
            except ValueError:
                print("Deposit amount must be a valid number.")
                return
            self.balance += deposit_amount
        return

    def withdrawal(self): 
        if player_choice == 2:
            print("How much would you like to withdraw?")
            withdraw_amount = (input(""))
            try:
                withdraw_amount = float(withdraw_amount)
            except ValueError:
                print("Withdrawal amount must be a valid number.")
                return
            if withdraw_amount < self.balance:
                self.balance -= withdraw_amount
            elif withdraw_amount > self.balance:
                print("Withdrawal amount cannot exceed the balance.")
        return

    def account_information(self):
        if player_choice == 3:
            print(f"Name: {self.name}")
            print(f"Account #: {self.account_number}")
            print(f"Balance: ${self.balance:.2f}")
        return
    
    def quit(self):
        if player_choice == 4:
            print("Thank you for your business!")
            exit()
