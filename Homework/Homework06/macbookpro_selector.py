# Sebastian Main
# Total time spent = 2 hours

def get_user_size():
    size = input("Choose a size ( 14 in. or 16 in. ): ")
    if size == "14":
        get_user_14chip(size)
        return size
    if size == "16":
        get_user_16chip(size)
        return size
    else:
        print("Sorry, we do not have a size " + str(size) + " inch")
        get_user_size()
        return size
        
    
def get_user_14chip(size):
    while size == "14":
        chip = input("Choose a chip ( M3, M3 Pro, M3 Max ): ")
        if chip == ("M3"):
            print("\nYou have chosen a MacBook Pro 14 inch with an M3 Chip.")
            print("\033[1mSpecifications:\033[0m")
            print("	8-core CPU")
            print("	10-core GPU")
            print("	8GB unified memory")
            print("	512GB SSD Storage")
            print("\033[1mPrice:\033[0m $1599")
            break
        if chip == ("M3 Pro"):
            print("\nYou have chosen a MacBook Pro 14 inch with an M3 Pro Chip.")
            print("\033[1mSpecifications:\033[0m")
            print("	11-core CPU")
            print("	14-core GPU")
            print("	18GB unified memory")
            print("	512GB SSD Storage")
            print("\033[1mPrice:\033[0m $1799")
            break
        if chip == ("M3 Max"):
            print("\nYou have chosen a MacBook Pro 14 inch with an M3 Max Chip.")
            print("\033[1mSpecifications:\033[0m")
            print("	14-core CPU")
            print("	30-core GPU")
            print("	36GB unified memory")
            print("	1TB SSD Storage")
            print("\033[1mPrice:\033[0m $3199")
            break
        else:
            print("Sorry, we do not have a " + str(chip) + " chip.")
            get_user_14chip(size)
            return chip
                
def get_user_16chip(size):          
    while size == "16":
        chip = input("Choose a chip ( M3 Pro, M3 Max ): ")
        if chip == ("M3 Pro"):
            print("\nYou have chosen a MacBook Pro 16 inch with an M3 Pro Chip.")
            print("\033[1mSpecifications:\033[0m")
            print("	12-core CPU")
            print("	18-core GPU")
            print("	18GB unified memory")
            print("	512GB SSD Storage")
            print("\033[1mPrice:\033[0m $2499")
            break
        if chip == ("M3 Max"):
            print("\nYou have chosen a MacBook Pro 16 inch with an M3 Max Chip.")
            print("\033[1mSpecifications:\033[0m")
            print("	14-core CPU")
            print("	30-core GPU")
            print("	36GB unified memory")
            print("	1TB SSD Storage")
            print("\033[1mPrice:\033[0m $3499")
            break
        else:
            print("Sorry, we do not have a " + str(chip) + " chip.")
            get_user_16chip(size)
            return chip


def main():
    size = get_user_size()
    

main()