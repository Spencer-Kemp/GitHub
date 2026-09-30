# Coding done by Spencer Kemp
# Changed variables to snake case
money_list = []
small_purchase = 0
medium_purchase = 0
large_purchase = 0
num_purchase = 0

# Creation of the user's shopping spree
while 0 not in money_list:
    
    money_input = float(input("Enter an expense or 0 to finish: "))
    money_input = int(money_input * 100) / 100
    if money_input >= 0:
        money_list.append(money_input)
        num_purchase += 1
        
        
        if money_input > 0 and money_input < 25:
            small_purchase += 1
        elif money_input >= 25 and money_input <= 100:
            medium_purchase += 1
        elif money_input > 100:
            large_purchase += 1
    else:
        print("Number can't be negative.")
        continue

# New variables
num_purchase = num_purchase - 1
money_list = money_list[:-1]

total_cost = sum(money_list)
average_cost = total_cost / len(money_list)
average_cost = int(average_cost * 100) / 100
smallest_cost = min(money_list)
largest_cost = max(money_list)

# Displaying the user's shopping spree
print("\n""Expense Summary")
print("-----------------")
print(f"Number of expenses: {num_purchase}")
print(f"Total: ${total_cost}")
print(f"Average: ${average_cost}")
print(f"Smallest expense: ${smallest_cost}")
print(f"Largest expense: ${largest_cost}")
print("\n"f"Small expenses: {small_purchase}")
print(f"Moderate expenses: {medium_purchase}")
print(f"Large expenses: {large_purchase}")