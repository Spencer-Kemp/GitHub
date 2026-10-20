def withdraw(amount, balance):
    if amount > balance:
        raise Exception("Insufficent Funds")

    return balance - amount