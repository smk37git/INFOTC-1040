"""
# Calculate the area of a triangel
a = input("Enter base: ")
a = float(a)
if a > 0:    # Remember to type Colon (:)
    print(a)
    
b = input("Enter height: ")
b= float(b)
if b > 0:5
    print(b)
# If condition will only execute if the condition is satisfied

c = a*b/2
if c >= 0:
    print("Area of the trinagle: " +str(c))
elif c < 0:
    print("Negative Area Error")
# Area of the Triangle is calculated

# run test cases
# edge case(s) -


# Conditional Executions
# Allows the execution to skip some code or run alternative code
# With conditionals: check if length is greater than or equal to 0
# Only do the calculation if the condition is satisfied

# Boolean datatype -- NOT STRINGS
# print(True)
# print(Flase)
"""




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
if x == y:  #two equality signs
    print("x is equal to y")
    
if x !=  y:
    print("x is not equal to y")
"""


"""
# Will print True if the first one is larger
# Will print False if the first one is equal to second or smaller than second
print(512/3*5 > 235/2*6)

# Logical Operations: and, or, not
x = 5
print(x>0 and x<10) # True if x is between 0 and 10
print(x>0 and x%2==0) # True if x is a positive even number
print(x<0 or x%2==1) # True if x is either negative or odd
print (not x<0) # True if x is not less than - - equivalent to x >=0
"""

length = float(input("Enter a length: "))
# length > 0: a Boolean expression, True or Flase
if length > 0: # header
    print("Length is positive.") # body --> commands will only run if inside body and condition is met
width = float(input("Enter a width: "))
if width > 0:
    print("Width is positive.")
    
# Check if length and width are both positive in one if statement
if (length > 0) and (width > 0):
    print("Both length and width are postive.")
    area = length * width
    print("The area is: " + str(area))
else:
    print("Either length or width is negative.")
