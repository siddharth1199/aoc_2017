#part i

data = open("input.txt", "r").read()

up_flights = data.count("(")
down_flights = data.count(")")
print(up_flights - down_flights)


#part ii


j = 0
i = 0
while i >=0:
    element = data[j]
    # Test for this element.
    if element == "(":
        i += 1
        j += 1
    if element == ")":
        i -=1
        j += 1
    # Display element.
print(j)
