"""
print("Integer Division")
print(4//2)

print("Exponentiation")
print(2**4)

print("Modulus")
print(6%4)

# addition and multiplication operators can be used with strings
# addition +
# restriction: BOTH Operands have to be strings
print("Hello" + " World!") # This is string concatenation --> gives one single string
# str()
# Take an integer or a float, and convert it to a string
print(str(1) + " cat")
print(str(3.2) + " dog")

# multiplication
print(5 * "abc") # "abc" + "abc" + "abc" + "abc" + "abc"
print ("abc" * 5) # same thing
"""
"""
# Variables
print(5.2 * 10) #calculate the area of a rectangle with a length of 5.2 and width 10
# Variable: A vlaue with a name
# Create a variable to store the length
# An assignment -- a special kind of statement
length = 5.2 # could also be (a)
width = 10 # could also be (b)
print(length*width)
# Can also condese it further
area = length * width
print(area)
"""
"""
#   Mini-Assignment
# Ask for user input
# Write a program that can calculate the area of a rectangle given the length and width
# 1. Ask the user for the length
a = input("Enter Length: ")                  # Pauses the execution of the program --> User types in --> returns it as str
print(a)
a=int(a)
# 2. Ask the user for the width
b = input("Enter Width: ")
print(b)
b=int(b)
# 3. Print the result -- area
c = a * b
print("Area: " + str(c))
"""
x = input("Enter x-value: ")
x=int(x)
if x > 0: # called a condition
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is equal to zero")
y=(5)
if x == y:
    print("x is equal to y")







