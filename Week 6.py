"""
# Monday Lecuture that I missed
# Initalize the counter:
i = 0
while i < 21:
    print(i)
    i += 1

# For counter in the_sequence_of_things_we_are_looping_over:
# sequences: strings, lists
# string: a sequence of characters "cat"
# lists: a sequence of anything [1, 2, 3]
print("Using list:")
for i in [1, 2, 3]:
    print(i)
    
print("Using range:")
# range (x,y): start from x, increment by 1, stop before y
for i in range(1,6):
    print(i)
 

# range(n):
r = range(5)
l = list(r) # convert the range r to a list
print(l)
"""
"""
fruit = "apple"
# i is the index
# the actual item is fruit[i]
for i in range(len(fruit)):
    # print(i) # i will be the index of the characters in fruit
    # print(fruit[i])
    print("The character at index " + str(i) + " is " + fruit[i])

l = [3,10,2,5]
for i in range(3, 4): # i will take 0, 1, 2, 3, for each iteration
    print("The number at index " + str(i) + " is " + str(l[i]))
    
# string: a sequence of characters
for c in fruit:
    print("c = " + c)
"""  
"""
i = 0
while i < 5:
    print("The character at index " + str(i) + " is " + fruit[i])
    i += 1
"""
"""
# Calculate the square of each number in a list
l = [1, 3, 10, 2, 8]

# While loop version:
print("While Loop Version:")
i = 0
while i < len(l):
    item =  l[i]
    result = item * item
    print(result)
    i += 1

# For loop version:
print("For Loop Version:")
for i in range(len(l)):
    item = l[i]
    result = item * item
    print(result)
    
for i in l:
    result = i * i
    print(result)
"""
# Wednesday
"""
ls = [1, 3, 5, 7, 9]
# While Loop
i = 0
while i < len(ls):
    item = ls[i]
    result = item * item
    print("The square of " + str(item) + " is " + str(result))
    i += 1
    
# For Loop
for i in range(len(ls)):
    item = ls[i]
    result = item * item
    print("The Square of " + str(item) + " is " + str(result))
    
# For Loop 2
for item in ls:
    result = item * item
    print("The Square of " + str(item) + " is " + str(result))
"""
"""

def get_direction(highway):
    if highway % 2 == 0:
        return"Direction is east / west."
    else:
        return "Direction is north / south."

def get_user_input():
    highway = int(input("Please enter an integer 1-99: "))
    while highway < 1 or highway > 99:
        highway = int(input("Please enter an integer 1-99: "))
    return highway
    
def main():
    highway = get_user_input()
    direction = get_direction(highway)
    print("Primary highway " + str(highway) + " goes " + direction)
    
main()
"""
"""
user_input = input("Please enter 1-99: ")

while user_input != "stop":
    highway = int(user_input)
    if highway % 2 == 0:
        print("East / West.")
    else:
        print("North / South.")
    user_input = input("Please enter 1-99: ")
    
print("While loop ends here.")
"""
"""
# Friday Lecture
user_input = input("Enter a number: ")
total = 0
while user_input != "done":
    n = float(user_input)
    total = total + n
    user_input = input("Enter a number:")
    # print(user_input)
    
print("Total = " + str(total))



# Nested If Statement
n = 10
if n > 0:
    print("n is positive.")
    if n % 2 == 1:
        print("n is positive and odd.")
    else:
        print("n is positive and even.")
else:
    print("n is non-positive.")
"""
# For Loops
# Ask the user to enter all the inputs

s = input("Please enter the numbers: ")
# split - given a string, split it into a list of substrings
# Called a dot notation
tokens = s.split()
# Use a for loop
# For every token--a string-- in the tokens list,
# convert it to an integer
total = 0
for token in tokens:
    n = float(token)
    print(str(n) + "^2 = " + str(n*n))
    if n % 2 == 0:
        print(str(n) + " is even.")
    total += n
print(tokens)
print("Total = " + str(total))
"""
nums = [1, 2, 3]
for n in nums:
    print(n)
"""


