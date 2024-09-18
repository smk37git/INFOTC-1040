# First Exercise
# Given the price of gas per gallon and the number of gallons added, calculate the total price
"""
def cost (cost):
    cost = price*gas
    return cost

price = float(input("\033[1mHow much is gas per gallon? \033[0m"))
gas = float(input("\033[1mHow many gallons of gas? \033[0m"))
cost = cost (cost)
print("\n\033[1mThe total cost is: \033[0m" + str(cost))


# Random Value thing?
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
if x > y:
    print("X is larger.")
elif x == y:
    print("X and Y are equal.")
else:
    print("Y is larger.")
"""
"""
# Given three numbers, find out which one is larger
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
# First, find out which one is the largest
# Then of of the two left numbers, which one is larger
if x > y and x > z:
    print("X is the largest.")
    if z > y:
        print("Z is larger.")
    else:
        if z == y:
            print("Z and Y are equal.")
if y > x and y > z:
    print("Y is the largest.")
    if x > z:
        print("X is larger.")
    else:
        if x == z:
            print("X and Z are equal.")
if z > x and z > y:
    print("Z is the largest.")
    if y > x:
        print("Y is larger.")
    else:
        if y == z:
            print("Y and Z are equal.")
elif y == x == z:
    print("All numbers are equal.")
"""
"""
# Chapter 5
# The positions are called indices - index
# Indices have to be integers
# Indices start from 0

# b a n a n a
# 0 1 2 3 4 5

fruit = "banana"
letter = fruit[1]
print(letter)

i = 5
letter = fruit[5]
print(letter)

# What's the index of the last character in a string?
# -1 or the length of the string -1
# Count from the end of the string, start with -1

i = len(fruit)-1
print(fruit[i])
fruit[len(fruit)-1]

x = 5
x = x + 1
x += 1
print(x)

i = 0
while i < 5:
    print(i)
    i += 1
print("Finish counting")

while 2 < 3:
    print(2)
# Use Crtl + C to stop
"""
"""
# Exercise
fruit = "apple"

i = 0
print("The letter at index " + str(i) + " is " + fruit[i])
i += 1
print("The letter at index " + str(i) + " is " + fruit[i])
i += 1
print("The letter at index " + str(i) + " is " + fruit[i])
i += 1
print("The letter at index " + str(i) + " is " + fruit[i])
i += 1
print("The letter at index " + str(i) + " is " + fruit[i])
i += 1


# While loop version:
# Repeat 5 times
# 0, 1, 2, 3, 4
# Stop repeating once i pass 4
# Since i has to be an integer, stop when i becomes 5
# i is usually called the counter, counter variable, iterative variable
fruit = input("Please enter a fruit: ")
i = 0
while i < len(fruit):
    print("The letter at index " + str(i) + " is " + fruit[i])
    i += 1
"""
"""
# Friday
# We will calculate the square of numbers 1 - 20
i = 1
while i <= 20:
    x = i * i
    print(x)
    i += 1

# New datatype: list
# list = a sequence of anything
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
fruits = ["apple", "banana", "strawberry", "pineapple"] # A list of 4 strings
print(ls)

i = 0
while i < len(ls):
    print("The number at index " + str(i) + " is " + str(ls[i]))
    item = ls[i]
    print (item * item)
    i += 1
"""
    
# While the user input is not valid, ask for the use input again
# This one repeats
        
def print_direction(highway):
    if highway % 2 == 0:
        print("Primary Highway " + str(highway) + " goes east / west.")
    else:
        print("Primary Highway " + str(highway) + " goes north / south.")

def check_user_input(highway):
    while highway < 1 or highway > 99:
    highway = int(input("Please enter a number (1-99): "))
    
def main():
    

main(highway)