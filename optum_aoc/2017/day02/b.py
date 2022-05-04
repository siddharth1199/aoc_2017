import sys
from itertools import permutations


def parse_inputs(filepath):
    with open(filepath, 'r') as f:
        grid = [[int(e) for e in l.split()] for l in f]
    return grid


def min_max_diff(row):
    return max(row) - min(row)


def evenly_divide_ratio(row):
    for x, y in permutations(row, 2):
        if x % y == 0:
            return x // y

    return None


def checksum_grid(grid, func):
    return sum(func(row) for row in grid)


def main(filepath):
    grid = parse_inputs(filepath)
    print(checksum_grid(grid, min_max_diff))
    print(checksum_grid(grid, evenly_divide_ratio))


if __name__ == '__main__':
    args = sys.argv
    print(args)
    if len(args) == 2:
        filepath = args[1]
    elif len(args) == 1:
        filepath = 'input.txt'
    else:
        raise ValueError('Example use: python3 solution.py [filepath]')

    main(filepath)