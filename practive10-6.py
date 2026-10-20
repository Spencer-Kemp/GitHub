numbers = [1, 2, 3, 4, 5]

#from "file name" import is_odd # this imports only is_odd from the other file
#import "file name" # this imports all the functions in that file

odd = 25
def is_odd(numero):
    global odd
    odd = True
    if numero % 2 ==0:
        odd = False
    if numero % 2 !=0:
        odd = True
    return odd

# is_odd = lambda numero: numero % 2 != 0

for num in numbers:
    if is_odd (num):
        print(f"{num} is odd.")
    else:
        print(f"{num} is even.")

print(odd)