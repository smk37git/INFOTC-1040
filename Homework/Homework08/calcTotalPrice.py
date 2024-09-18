# Sebastian Main


def main():
    f = open("shoppingCart.txt")
    total_cost = 0
    for lines in f:
        line = lines.split(",")
        print(line[0])
    f.close()
    


main()



#print("For " + line[0] + " the price is $" + line[1] + " and there are " + line[2])
        #cost = float(line[1]) * float(line[2])
        #total_cost += cost
    #print("Total Price: $" + str(total_cost)) 