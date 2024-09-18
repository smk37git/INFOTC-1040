# Monday Lecture
"""
class NPC:
    def __init__(self, n, c, p):
        self.id = n
        self.color = c
        self.position = p
        
    def paint(self, new_color):
        self.color = new_color
        
    def move_forward(self, k):
        self.position += k
        return self.position
    
    def __str__(self):
        # return the string you want to see when you later print the object
        return f"NPC{self.id} - color: {self.color} - position: {self.position}"

def main():
    NUMBER_OF_NPCS = 0
    NUMBER_OF_NPCS += 1
    npc1 = NPC(NUMBER_OF_NPCS, "black", 0)
    
    print(npc1)
    #npc1.id = 1
    #npc1 = NPC()
    print(npc1)
    
    NUMBER_OF_NPCS += 1
    npc2 = NPC(NUMBER_OF_NPCS, 2.5, "red")
    #npc2.id = 2
    #npc2 = NPC()
    #npc1.print_npc() # Traditional way
    #NPC.print_npc(npc2) # New "easier" way
    
    npc2.paint("red")
    print(f"npc2's color is changed to {npc2.color}")
    
    npc1.move_forward(5)
    print(f"npc1 is moved to positon {npc1.position}")
    npc1.move_forward(3)
    print(f"npc1 is moved to positon {npc1.position}")
    
main()
"""
# End of Lab
# RECURSION DEMO
# Kinds of statements:
# 1. assignment: var = val
# 2. if statement
# 3. while loop
# 4. for loop
# 5. a function call

# A recursive function is a function that calls itself.
# Important: Base case -- where the recursive calls stop
# Example: print 5 times.
# Create a counter, starting at 0
# When it reaches 5, stop.
# Before it reaches 5, print, then increment counter by 1
#counter = 0 # variable outside the function
 
"""
#1. Recursion is not necessary. Recursion and loop are equivalent.
#2. For some problems, recursion version is easier to understand and to write.
"""

def print_rec(name, counter):
    if counter < 5:
        print(f"Hello, {name}!")
        counter += 1
        print_rec(name, counter) # Call the function itself
# counter is a parameter
print_rec("Melon",  0)

# length of a list = 1 + length of l[1:]
# [1, 2, 3, 4]
# 1 + length of [2, 3, 4]
# 1 + (1 + length [3, 4])
# 1 + (1 + (1 + length [4]))
# 1 + (1 + (1 + (1 + length [])))
def length(l):
    if l == []:
        return 0
    else:
        return 1 + length(l[1:])
# Fibonacci number:
# 1, 1, 2, 3, 5, 8, 13, 21, 34...
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

nums = [3, 4, 5, 6, 7]
print(length(nums))
print(fib(10))
n = 25
print(f"The {n}th fibonacci number is {fib(n)}")