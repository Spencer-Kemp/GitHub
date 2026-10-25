from level08AssignmentFunctions import BankAccount

print("Welcome to the cool bank")

print("Please enter your name: ")
account_name = input("")

account1 = BankAccount(account_name)

while True:
    account1.display_options()
    account1.deposit()
    account1.withdrawal()
    account1.account_information()
    account1.quit()
