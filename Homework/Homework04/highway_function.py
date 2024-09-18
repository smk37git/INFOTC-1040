# Sebastian Main
# Problem #1
def get_direction(highway):
    if highway % 2 == 0:
        return "East / West."
    else:
        return "North / South."
        
def main():
    highway = int(input("Please enter a primary highway number (1-99): "))
    direction = get_direction(highway)
    print("Primary highway " + "\033[1m" + str(highway) + "\033[0m" + " goes " + "\033[1m" + str(direction) + "\033[0m")
    
main()