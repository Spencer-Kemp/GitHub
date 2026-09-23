# add the while loops as you need them while coding.
# Code from the inside out.

# an array - numbers = [5, 16, -3] ( its a list)

myList = [3, 8, 27, 7, -9]
positive = 0
negative = 0
zero = 0

for i in myList:
    if i > 0:
        print (f"{i} is a positive number")
        positive += 1
    elif i < 0:
        print (f"{i} is a negative number")
        negative += 1
    elif i == 0:
        print (f"{i} is equal to zero")
        zero += 1

print (f"There are {positive} positive number(s), {negative} negative number(s), and {zero} zero(s).")
print()