# Week 10 -- Monday Lecture -- WRITING TO FILE + DICTIONARIES
"""
# WRITING TO FILE
# To read a file:
# 1. Open the file

#f = open("readFromFile.txt")    # The file is open in READ mode by default
#f = open("readFormFile.txt", "r") # "r" is for read mode. Same as above.
# for line in f:
# f.readlines() then a for loop
# f.read() # A big string with entire content
#f.close()

# If the file with the name doesn't exist, then Python will create an empty file with that name in the same folder as your program
# if the File already exists, then Python will wipe it clean.
# "w" write mode is actually OVERWRITE mode.
f2 = open("writeToFile.txt", "w")
# To write to a file: argument is ONE string
f2.write("Text would go here\n")
f2.write("Hello World!")
# NOTE:
# 1. It only accepts one arguement -- one string. Use f-string or string concatenation to make sure it's one string
# 2. write() doesn't automatically add the new line character at the end.
# 3. It only accepts string. Doesn't write integers, floats, anything except for string.

f2.close()    # MUST CLOSE THE FILE

# Append mode
f2 = open("writeToFile.txt", "a")
f2.write("This is written in append mode.")
f2.close()
"""
"""
# DICTIONARIES

l = [] # empty list
l.append("Tulip") # To add element to l: append()
l.append(2)
print(l)

d = {} # Empty dictionary
# To add element to d:
# d[key] = value
d["tulip"] = "any of a genus (Tulipa) of Eurasian bulbous herbs of the lily family"
print(d)
d["mourning cloak"] = "a blackish - brown nymphalid butterfuly (Nymphalis antiopa) that"
print(d)
# Access the value of a key: dictionary)name[key]
print("Meaning of tulip: " + d["tulip"])
print("Meaning of mourning cloak: " + d["mourning cloak"])

# Things to notice:
# 1. No duplicate keys
# 2. Value can be any datatype; Key have to be immutable datatype -- everything except for list and dictionary
illegal_d = {}
illegal_d[[1, 2, 3]] = 1
"""
# Wednesday Lecture
"""
num2eng = {} # empty dictionary
# Add an element
# d[key] = val
num2eng[1] = "one"
num2eng[2] = "two"
num2eng[3] = "three"
print(num2eng)
print(len(num2eng)) # get the number of elements in a dictionary

# []: list, {}: dictionary, "": string
#d = {key1:val1, key2:val2, ...}
# : seperates key and value,
# , seperates elements
num2eng_v2 = {1:"one", 2:"two", 3:"three"}
print(num2eng_v2)

l = [1, 2, 3]
# in operator: checks an element/item exists in a list
print(2 in l)
# for a dictionary, in operator checks if a KEY exists in a list
print("Does 2 exist in the dictionary: ", 2 in num2eng)
for x in num2eng:
    print(x)
    val = num2eng[x] # The value for the key
    print(f"The value for key {x} = {val}")
"""
"""
prices_d = {"desk":129.9, "computer":1099, "lamp":30.5, "couch":550, "notebook":20.9}
#print("lamp" in prices_d)
#print(prices_d["couch"])

user = input("What do you want to buy? (name,quantity): ")
while user != "Done":
# Process the user input to get the name and the quantity
    tokens = user.split(",")   # Split the user input by comma, ["desk, "2"]
    name = tokens[0]
    quantity = int(tokens[1])
    # Check if the name of the item exists in the shop
    cart = {}
    if name in prices_d:
        # add to shopping cart
        # key: name of the item
        # value: quantity
        cart[name] = quantity
    user = input("What do you want to buy? (name,quantity): ")
print(cart)
"""
"""
# FRIDAY LECTURE
def main():
    # Define the dictionary
    # Name as key, price as value
    prices_d = {"desk":129.9, "computer":1099, "lamp":30.5, "couch":550, "notebook":20.9}
    # OR USE
    #prices_d = {}
    #prices_d["desk"] = 129.9
    #prices_d["computer"] = 1099
    
    # Cart is a dictionary
    # Item name was key, quantity as value
    # {"desk":2, "lamp":5}
    # Initial value for cart is:
    # 0 for every key
    cart = {}
    # for every key in prices_d, add an element to cart with key being the same key in prices_d, value 0
    for key in prices_d:
        cart[key] = 0
        
    # Update from Wednesday lecture: so prgram can allow user to add the same item multiple times
    
    # Ask user what item they want and how many they want
    user = input("What do you want to buy? (name,quantity): ")
    while user != "Done":
        tokens = user.split(",")
        print(tokens)
        name = tokens[0]
        quantity = int(tokens[1])
        print(f"You added {quantity} {name}s to the cart.")
        cart[name] += quantity   # Add the new element to the dictionary
        user = input("What do you want to buy? (name, quantity): ")
        # If we have the name in the cart: then add the new quantity to the current quantity.
        # Otherwise, cart[name] = quantity
        print(cart)
        
        #if name in cart:  # If key exists in dictionary
            # Current quantity: cart[name]
            #cart[name] += quantity
        #else:
            #cart[name] = quantity
        
    total = 0
    for key in cart:
        # get the quantity
        quantity = cart[key]
        # get the unit price
        unit_price = prices_d[key]
        total += quantity * unit_price
    print(total)

main()
"""
# Tuple
# A datatype for a collection of data
# It's almost the same as a list
# 1. Use () for tuple
tp = ("apple", "banana", "orange")
tp[0]
print(tp[0])

# 2. Tuple are immutable
l = ["apple", "banana", "orange"]
l[0] = "strawberry"
print(l)



