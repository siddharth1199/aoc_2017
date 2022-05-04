import sys
import numpy as np


def read_input(fname):
    values = []
    with open('input.txt', 'r') as f:
        for line in f:
            values.append([int(i) for i in line.strip().split('\t')])

    values = np.array(values)
    values.sort(axis=1)
    return values


def solve(values, part_num):
    if part_num == 1:
        return (values[:, -1] - values[:, 0]).sum()
    elif part_num == 2:
        sum_val = 0
        # Small optimization on calculations by looking at pairs that are more likely to be divisible first.
        # This is done by working with sorted array and loop through each row from opposite directions
        for i in range(values.shape[0]):
            pair_found = False
            for j in reversed(range(values.shape[1])):
                large_val = values[i, j]
                for k in range(0, j):
                    small_val = values[i, k]
                    if large_val % small_val == 0:
                        pair_found = True
                        sum_val = sum_val + int(large_val / small_val)
                        break
                if pair_found:
                    break
        return sum_val


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 1

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    values = read_input(input_file)
    print(solve(values, part_num))