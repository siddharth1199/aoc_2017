file = open('input.txt', 'r')

current_floor = 0
current_position = 0
basement_position = 1
basement_not_found = True

while True:
    # read by character
    char = file.read(1)

    if not char:
        break

    if char == '(':
        # go up a floor
        current_floor += 1
    elif char == ')':
        # go down a floor
        current_floor -= 1

    current_position += 1

    if basement_not_found & (current_floor < 0):
        basement_position = current_position
        basement_not_found = False

file.close()

print('current floor is {}.'.format(str(current_floor)))
print('basement reached on position {}.'.format(str(basement_position)))