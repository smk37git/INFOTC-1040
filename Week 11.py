# Wednesday Lecture
# Object-oriented programming

# A class has two parts:
# data and methods
"""
class Person:
    # define the initializer
    # it creates/defines the attributes of the class
    # assigns default values to the attributes
    
    def __init__(self):
        self.first_name = "Jon"
        self.last_name = "Doe"
        self.age = 1
"""        
# Lab example       
        
# Find the definition of NPC class
# Execute the initalizer of NPC
# Create an object from the NPC class
# Create the three attributes for the object
# Assign the default values to the attributes
# npc1
# npc1.id: 0
# npc.color: "white"
# npc1.position: 0.0

class NPC:
    def __init__(self, n, c, p):
        self.id = n
        self.color = c
        self.position = p
        
    def paint(self, new_color): # Change the color of the object to the new color
        # DO NOT WRITE npc.color = new_color
        # DO NOT WRITE npc1.color = new_color
        self.color = new_color
        
    def move_forward(self, k):
        # calculate the new position
        # current position + k
        self.position += k
        return self.position
        
    def print_npc(self):
        # print all three attributues nicely
        x = self.id
        c = self.color
        p = self.position
        print(f"id: {x}")
        print(f"color: {c}")
        print(f"position: {p}")
        

def main():
    NUMBER_OF_NPCS = 0
    
    NUMBER_OF_NPCS += 1
    npc1 = NPC(NUMBER_OF_NPCS, "black", 0)
    
    #npc1.id = 1
    #npc1 = NPC()
    print(npc1)
    
    NUMBER_OF_NPCS += 1
    npc2 = NPC(NUMBER_OF_NPCS, 2.5, "red")
    #npc2.id = 2
    #npc2 = NPC()
    npc1.print_npc() # Traditional way
    NPC.print_npc(npc2) # New "easier" way
    
    npc2.paint("red")
    print(f"npc2's color is changed to {npc2.color}")
    
    npc1.move_forward(5)
    print(f"npc1 is moved to positon {npc1.position}")
    npc1.move_forward(3)
    print(f"npc1 is moved to positon {npc1.position}")

main()