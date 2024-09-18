f = open("mbox_short.txt")
# Don't Forget to close the file
#content = f.read()
#print(content)
"""
# Read the file line by line -- with line number
lines = f.readlines() # a list of strings, each string is one line
for i in range(len(lines)):
    line = lines[i]
    print(f"line #{i}: {line}")
    """
# How many emails from ___ email address.



counter = 0
for line in f:
    start_with = line[:5]
    if start_with == "From:":
        rest = line[5:]
        rest = rest.strip()
        if rest == "rjlowe@iupui.edu":
            counter += 1
print("Number of emails from rjlowe@iupui.edu: " + str(counter))

f.close()