# Sebastian Main
def get_cel(temp):
    if temp >= -459.67:
        Cel = (temp - 32)*(5/9)
        return Cel
        
def get_user_input():
    temp = float(input("Please enter a Fahrenheit temperature: "))
    while temp < -459.67:
        temp = float(input("Please enter a Fahrenheit temperature: "))
    return temp

def main():
    temp = get_user_input()
    celsius = get_cel(temp)
    print(str(temp) + "F = " + str(celsius) + "C")
          
main()