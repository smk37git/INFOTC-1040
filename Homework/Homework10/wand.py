# Sebastian Main

class wand:
    def __init__(self, l, w, c, o):
        self.length = l
        self.wood = w
        self.core = c
        self.owner = o
        
    def defeated_by(self, new_owner):
        self.owner = new_owner
        return self.owner
        
    def __str__(self):
        return f"\nLength: {self.length} \nWood: {self.wood} \nCore: {self.core} \nOwner: {self.owner}"
    
        
def main():
    number_of_wands = 0
    number_of_wands += 1
    wand_1 = wand(15, "elder", "thestral tail hair", "Albus Dumbledore")
    print(wand_1)
    wand_2 = wand(10, "hawthorn", "unicorn hair", "Draco Malfoy")
    print(wand_2)
    wand_3 = wand(11, "holly", "phoenix feather", "Harry Potter")
    print(wand_3)
    
    wand_1.defeated_by("Draco Malfoy")
    print(wand_1)
    
    wand_1.defeated_by("Harry Potter")
    print(wand_1)

    
    
main()