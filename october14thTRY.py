
has_error = True

while has_error: # The "has_error" variable
    # Any error we get, we go to the except
    try:
        number = int(input("Enter a number: "))
        print (number)
        has_error = False
        
    except ValueError:
        print("invalid number. Please try again.")
    except KeyboardInterrupt:
        print("You stopped the program!")
    except:
        print("You got some rando error")
        break
        has_error = True
        continue 
    else: # If there is no error it will do the else
        print("You entered a valid number! Amazing!")
    finally: # Will run no matter what at the end of the try block
        print("Got through it!")