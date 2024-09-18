# Monday Lecture
"""
brand = "Ford"
print(brand[0])
print(brand[1])
print(brand[2])
print(brand[3])

l = len(brand) # Get hte length - the number of characters in the string
print("Length = " + str(l))

# Slice: A continous segment of a string -- Same as a substring
brand2 = "Volkswagen"
# V o l k s w a g e n
# 0 1 2 3 4 5 6 7 8 9
slice1 = brand2[3:7]
print("Slice1 = " + slice1)
slice2 = brand2[3:4]
print("Slice1 = " + slice2)

# Rest of string starting from an index
slice7 = brand2[5:]
print(slice7)
"""

# Wednesday Lecture

s = "banana"
print("b" in s)
print("c" in s)
print("ban" in s)
print("banan" in s)
print("banana" in s)
print("banaa"in s)

s = "Current time: 08:00am"
tokens1 = s.split()
print(tokens1)

tokens2 = s.split("Current Time:")
print(tokens2)


time = input("Please enter a time (24 hour format): ")
print("The time entered = " + time)
tokens3 = time.split(":")
print("tokens3 = " + str(tokens3))
hour = int(tokens3[0])
minute = int(tokens3[1])
print("Hour = " + str(hour))
print("Minute = " + str(minute))



s = "  a    b    c   "
s2 = s.strip()
print(s2)
s3 = s.strip("  a")
print(s3)

s = "          Current              time: 08:00am"
s2 = s2.split()
tokens2 = s.split(":")
for token in tokens2:
    print(token.strip())

n = 10
# calculate the square of n
# goal: 10^2 = 100

print(str(n) + "^2 = " + str(n*n))
print(f"{n}^2 = {n * n + 2 * 100}")

