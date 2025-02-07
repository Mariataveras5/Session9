fp = open("text.txt", "r")
print(fp.read())
fp.close() #close is good practice, not needed in this example

#same thing but more pythonic
with open("text.txt", "r") as fp: #this creates a context
    print(fp.read())

print("We are done, the context is closed by the indent")

# read from the same file, line by line, adds an extra space between each line
with open("text.txt", "r") as fp:
    line_number = 1
    for line in fp:
        # print(line, end="") end eliminates the extra space
        # print(line.rstrip()), we are using a formated string (fstring)
        print(f"{line_number}: {line.rstrip()}")
        line_number += 1

