# open()
# Filename: a string, include the extension
# return a file object
# NOT THE CONTENT of the file
f = open("numbers.txt")

# To get the cotent of the file

# Method 1: the entire content as one single string
# f.read()
"""
content = f.read() # Content is a string
print(content)
# new line character: \n

print("Hello\nWorld")
print("Hello World")

s = "a\nb" # Length is 3, NOT 2
print("Length of s = " + str(len(s)))
"""
"""
# Method 2: get a list of strings, each string is one line.
lines = f.readlines()
#print(lines)

for line in lines:
    print(line)
    
"""
# Method 3: without using any functions
# No line number
for line in f:
    print(line)
f.close()
f = open("numbers.txt")
for line in f:
    print(line)
f.close()

"""
# 1. Open the file
# 2. Process the data
# 3. Close the file
"""
