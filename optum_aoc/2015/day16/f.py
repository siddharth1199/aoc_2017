import re
import sys

REFERENCE = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
             'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2,
             'perfumes': 1}

GREATER = {'cats', 'trees'}
FEWER = {'pomeranians', 'goldfish'}


def parse_input(input_path='input.txt'):
    pattern = re.compile(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')

    with open(input_path) as f:
        for line in f:
            aunt_idx, compound1, val1, compound2, val2, compound3, val3 = re.match(pattern, line).groups()
            yield aunt_idx, {compound1: int(val1), compound2: int(val2), compound3: int(val3)}


def solve(data):
    for aunt_idx, aunt_info in data:

        # part 1
        for key in aunt_info.keys():

            if aunt_info[key] != REFERENCE[key]:
                break
        else:
            print('Answer for part 1: {}'.format(aunt_idx))

        # part2
        for key in aunt_info.keys():

            compound_val = aunt_info[key]

            if key in GREATER:
                if compound_val <= REFERENCE[key]:
                    break
            elif key in FEWER:
                if compound_val >= REFERENCE[key]:
                    break
            else:
                if compound_val != REFERENCE[key]:
                    break
        else:
            print('Answer for part 2: {}'.format(aunt_idx))
            break
    return


def main():
    if len(sys.argv) < 2:
        data = parse_input()
    else:
        data = parse_input(sys.argv[-1])

    solve(data)


if __name__ == '__main__':
    main()
