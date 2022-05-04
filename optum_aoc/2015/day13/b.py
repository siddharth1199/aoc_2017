from functools import lru_cache
import sys

HAPPINESS_SIGN = {'gain': +1, 'lose': -1}

happiness_table = {}


def generate_happiness_table(fname):
    guests = set()
    with open(fname, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            tokens = line[:-1].split()

            first = tokens[0]
            second = tokens[-1]
            key = (first, second) if first > second else (second, first)

            guests.add(first)

            value = HAPPINESS_SIGN[tokens[2]] * int(tokens[3])
            happiness_table[key] = happiness_table[key] + value if key in happiness_table.keys() else value

    return list(guests)


def get_happiness(first, second):
    return happiness_table[first, second] if first > second else happiness_table[second, first]


# Seating two guests at a time keeping track of start and end of seated guests
@lru_cache
def calculate_happiness(not_seated, first, last):
    if len(not_seated) == 0:
        return get_happiness(first, last)
    if len(not_seated) == 1:
        return get_happiness(first, list(not_seated)[0]) + \
               get_happiness(list(not_seated)[0], last)

    return max([get_happiness(new_first, first) + \
                calculate_happiness(frozenset(not_seated - set([new_first, new_last])), new_first, new_last) + \
                get_happiness(new_last, last) for new_first in not_seated for new_last in not_seated if
                new_first != new_last])


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 2

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    guests = generate_happiness_table(input_file)

    if part_num == 2:
        # Using ZZZ to avoid checking order when generating dictionary keys
        for guest in guests:
            happiness_table[('ZZZ', guest)] = 0
        guests.append('ZZZ')

    print(max(
        [calculate_happiness(frozenset(set(guests) - set([i, j])), i, j) + get_happiness(i, j) for i in guests for j in
         guests if i != j]))
