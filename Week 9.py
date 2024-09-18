"""
s = input("Enter a number 1-99: ")
# 1. Write code without try-except
# 2. Run with inputs that will break the code (give an error)
# 3. See which line the error is one
# 4. Put it in the else block together with the calculation.

# Try to convert s into an integer)
 # If something goes wrong, i.e., s cannot be converted to integer.

# The condition is always true
# An Infinite loop
# TO break from a loop: use keyword "break"
# End the loop, continue the executing the code after the loop
while True:
    try:
        n = int(s)
    except:
        print("Input should be an integer.")
        s = input("Enter a number 1-99: ")
    else:
        if n > 0 and n < 100:
            break
        else:
            print("Invalid highway number.")
            s = input("Enter a number 1-99: ")
     
# If everything goes well, i.e., s can be converted to int.
if n % 2 == 0:
    print("East/West")
else:
    print("North/South")
"""
            
try:
    x = x + 5
except NameError: # Only catch the NameErrors
    print("Something went wrong.")
except IndexError: # Only catch the IndexErrors
    print("Index out of range")
    

