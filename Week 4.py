"""
# Example from Friday (Week 2)
length = float(input("Enter a length: "))
if length > 0:
    print("Length is positive.")
width = float(input("Enter a width: "))
if width > 0:
    print("Width is positive.")
    
if (length > 0) and (width > 0):
    print("Both length and width are postive.")
    area = length * width
    print("The area is: " + str(area))
    
else:
    if length <= 0:
        print("Length is invalid")
    if width <= 0:
        print("Width is invalid")
        
# Below not needed
elif length <=0:
    print("Length is invalid.")
elif width <=0:
    print("Width is invalid.")
    
elif length <= 0 or width <= 0:
    print ("Either length or width is negative.")
    
#else:
    #print("Either length or width is negative.")
"""

# FUNCTIONS
# print() / input() / float() / int() / str() / type()
# Function call: call the function print()
# Function Definition
# Arugements: The values or variables inside the parentheses when the function is called --> float(x) = x
# Return: Output of a function (return value) --> at most one value
    # When it doesn't return anything, its a void function.
""" 
hello()
Inputs: None
Output: None -- doesn't return anything
"""
# In the parentheses, we put the paramets --- which are called arguements when we call the function
# hello(): doesn't any have any parameters
# So when we call hello(), we should NOT provide any arguements

# Rewrite hello() so it can say hello to anyone given the person's name
# Rewrite hello() again so it can say hello to anyone and welcome them to any course
"""
def hello(person, course):
    # old - print("Hello, Coco!")
    print("\nHello " + person + "!")
    print("Welcome to " + course + "!")
    
# Do NOT use the parameters outside a function
    
person = input("\033[1mWhat is your name: ") # person: is a global variable
course = input("What is your course: \033[0m")
hello(person, course) # Postional arguements --- matches the parameters by position, NOT by variable name
"""
"""
# Create a function with the name calc_rec_area() that takes the length and width of a rectangle and prints the area of the rectangle
# 1. Add the inputs of the function as parameters to the parentheses
# 2. Move the taking-user-inuts part to the outside of the function definition
# 3. Add the arguments to the function.

# Should always seperate the I/O - input and output - from the actual calculation
def calc_rec_area(length, width):
    area = length*width
    return area # Local variable
    # Return terminates the execution of a function
    
length = float(input("\033[1mEnter the Length: "))
width = float(input("Enter the width: \033[0m"))
result = calc_rec_area(length, width) # Will have the value returned from the function and the values can be assigned to variables -- Global variable

print("\n\033[1mArea = \033[0m" + str(result))
"""
"""
# Yearly Wage
# We call main(), main() calls yearly_wage()
def yearly_wage(hours, wage):
    yearly_wage = hours * 365 * wage
    return yearly_wage
    
def main():    
    h = float(input("Enter the hours you worked daily: "))
    w = float(input("Enter your hourly wage: "))
    yearly = yearly_wage(h, w)
    print("yearly wage = " + str(yearly))

main()
"""

# Exercise
def calc_rec_area(length, width):
    area_rec = length * width
    return area

def calc_tri_area(base, height):
    area = base * height * 0.5
    return area

# User Inputs
shape = input("Do you want to calculate the area of a rectangle or a triangle? ")
if shape == "rectangle":
        print(shape)
        length = float(input("Enter a length: "))
        width = float(input("Enter a width: "))
        area = calc_rec_area(length, width)
        print("Area of the rectangle = " + str(area))
elif shape == "triangle":
        print(shape)
        base = float(input("Enter a base: "))
        height = float(input("Enter a height: "))
        area = calc_tri_area(base, height)
        print("Area of the triangle = " + str(area))




