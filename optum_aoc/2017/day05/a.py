def read_input(file_name):
    """ returns lines in a list  """
    with open(file_name) as file:
        lines = [int(i.strip('')) for i in list(file)]
    return lines


def part_one(lines):
    """ sum  of all places to jump will never be greater than length of lines"""
    place_to_jump, i, j = (0, 0, 0)
    while i < len(lines):
        place_to_jump = lines[i]
        lines[i] += 1
        i += place_to_jump
        j = j+1
    return j


def part_two(lines):
    """ adding the extra condition """
    place_to_jump, i, j = (0, 0, 0)
    while i < len(lines):
        place_to_jump = lines[i]
        if place_to_jump >= 3:
            lines[i] -= 1
        else:
            lines[i] += 1
        i += place_to_jump
        j = j+1
    return j

if __name__ == '__main__':
    lines = read_input('2017_day_5.txt')
    print('part one steps are {}'.format(part_one(lines)))
    lines = read_input('2017_day_5.txt')
    print('part two steps are {}'.format(part_two(lines)))