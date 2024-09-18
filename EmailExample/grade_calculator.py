filename = input("Please enter the name of the file: ")
# grades.txt
# Handle erros gracefully,
# 	1. print userful messages to the user
# 	2. Let the user try again

# Try to open file
# If python can open the file, meaning f = open(filename) will not give any errors
# Then open the file
# otherwise, don't open the file and print a message
while True:   # An always True condition
    try:
        f = open(filename) # Filename is a string
    except:
        print(f"File {filename} dones't exist. Please try again.")
        filename = input("Please enter the name of the file: ")
    else:
        lines = f.readlines()
        # Go through each line in the file
        #for line in f: # Will go through every line. But we want to skip the first line
        for i in range (1, len(lines)): 
            # Split the line by "," to get the tokens/parts
            line = lines[i]
            tokens = line.split(",")
            print(tokens)
            
            # Use different counters for nested loops
            final_grade = 0
            grades = [] # all 3 grades for the current student
            for j in range (1, len(tokens)):
                #print(tokens[j])
                n = float(tokens[j])
                grades.append(n)
            print(grades)
            final_grade = grades[0] * 0.3 + grades[1] * 0.3 + grades[2] * 0.4
            print("Final Grade = " + str(final_grade))

        f.close()
        break # break from the loop