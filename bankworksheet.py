from bankFunctions import withdraw

balance = 100

try:
    amount = int(input("Please enter the amount you would like to withdraw: "))

    balance = withdraw(amount, balance)
    print(balance)
except:
    print("Invalid amount")