# Coding done by Spencer Kemp

iMoneyList = []
iSmallPurchase = 0
iMediumPurchase = 0
iLargePurchase = 0
iNumPurchase = 0

# Creation of the user's shopping spree
while 0 not in iMoneyList:
    
    iMoneyInput = float(input("Enter an expense or 0 to finish: "))
    iMoneyInput = int(iMoneyInput * 100) / 100
    if iMoneyInput >= 0:
        iMoneyList.append(iMoneyInput)
        iNumPurchase += 1
        print(iMoneyList)
        print(iNumPurchase)
        if iMoneyInput > 0 and iMoneyInput < 25:
            iSmallPurchase += 1
        elif iMoneyInput >= 25 and iMoneyInput <= 100:
            iMediumPurchase += 1
        elif iMoneyInput > 100:
            iLargePurchase += 1
    else:
        print("Number can't be negative.")
        continue

# New variables
iNumPurchase = iNumPurchase - 1
iMoneyList = iMoneyList[:-1]
print(iMoneyList)
iTotalCost = sum(iMoneyList)
iAverageCost = iTotalCost / len(iMoneyList)
iAverageCost = int(iAverageCost * 100) / 100
iSmallestCost = min(iMoneyList)
iLargestCost = max(iMoneyList)

# Displaying the user's shopping spree
print("\n""Expense Summary")
print("-----------------")
print(f"Number of expenses: {iNumPurchase}")
print(f"Total: ${iTotalCost}")
print(f"Average: ${iAverageCost}")
print(f"Smallest expense: ${iSmallestCost}")
print(f"Largest expense: ${iLargestCost}")
print("\n"f"Small expenses: {iSmallPurchase}")
print(f"Moderate expenses: {iMediumPurchase}")
print(f"Large expenses: {iLargePurchase}")