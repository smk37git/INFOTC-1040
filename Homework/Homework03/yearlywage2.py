# Sebastian Main
# Problem #2
a = input("Enter the number of hours worked daily: ")
print(a)
a=float(a)
if a < 8:
    a=float(a)
if a > 8:
    hours = 8

b = input("Enter the hourly wage: ")
print(b)
b=float(b)

if a==8:
    c=a*b*365
    print("Yearly wage = " + str(c))
    
if a > 8:
    print("You will be compensated for working overtime.")
    d = a - 8
    d = float(d)
    e = d*b*2*365
    e = float(e)
    c=hours*b*365
    print("Yearly wage = " + str(c+e))
if a < 8:
    c=a*b*365
    print("Yearly wage = " +str(c))