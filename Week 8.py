# Monday Lecture -- Nested lists
# A nested list is a list of lists
# Example
"""
l = [[1, 2], [3], [4, 5, 6]]
print(l[0])
print(l[2])

l1 = l[0] # l1 is a list: [1,2]
print(l1[0])
# Takes a long time, to simplifiy:
print("The first item in the first sublist: " + str(l[0][0]))
print("The second item in the first sublist: " + str(l[0][1]))
print("The second item in the third sublist: " + str(l[2][1]))
"""

"""
# Matrix table
table = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11 ,12]]
"""

"""
print("Number of rows = " + str(len(table)))
print("Number of columns = " + str(len(table[0])))

# Examples
for row in table:
    print(row)
    print("Sum of the row = " + str(sum(row)))
    
# Go through each row, get the number at index 0 in each row
first_col = []
for row in table:
    print("First item in the row = " + str(row[0]))
    first_col.append(row[0])

print("First column = " + str(first_col))
print("The sum of the itmes in the first column = " + str(sum(first_col)))
"""

# Print every entry in a table
# Method 1: Without the indices
# Nested for loop
"""
for row in table:
        print(row)
        for item in row:
            print(item)

# Method 2: With the indices
# i for outer-loop
# j for inner-loop
# k for a third-level loop if needed
for i in range(len(table)):
    row = table[i]
    for j in range(len(row)):
        print(row[j])


harry = ["Harry", 30]
berry = ["Berry", 41.5]
tina = ["Tina", 53.4]

all_grades = [harry, berry, tina]
print(all_grades)

harry[1] = 60.7
print(all_grades)
"""


# Wednesday Lecture -- Files
# Check folder as "EmailExample" and emailFiter.py for notes.




