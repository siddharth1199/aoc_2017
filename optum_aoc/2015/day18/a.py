import numpy as np
import sys
import itertools
import copy

SWITCH_MAP = {'.': 0, '#': 1}
NUM_ITER = 100


def corner_cases(data, len_x, len_y, pass_corners=True):
    if pass_corners:
        data[[1, len_x - 2, len_x - 2, 1], [1, 1, len_y - 2, len_y - 2]] = True
    return data


def step(data, len_x, len_y, pass_corners):
    tot = sum(np.roll(data, shift, axis=(0, 1)) for shift in filter(any, itertools.product(range(-1, 2), repeat=2)))
    data[data & ~np.isin(tot, (2, 3))] = False
    data[~data & (tot == 3)] = True

    data[0, :] = data[-1, :] = data[:, 0] = data[:, -1] = False
    corner_cases(data, len_x, len_y, pass_corners)
    return data


def run_part(part_num, initial_data):
    if part_num == 1:
        data = copy.deepcopy(initial_data)
    else:
        data = initial_data
    len_x, len_y = data.shape
    pass_corners = False if part_num == 1 else True
    corner_cases(data, len_x, len_y, pass_corners)

    for _ in range(NUM_ITER):
        data = step(data, len_x, len_y, pass_corners)
    return sum(sum(data))


def main(file):
    with open(file, 'r') as f:
        initial_data = np.array([[SWITCH_MAP[i] for i in line.strip()] for line in f.readlines()]).astype(np.bool)
    initial_data = np.pad(initial_data, ((1, 1), (1, 1)), constant_values=0)

    for part_num in [1, 2]:
        print(f'For Part number {part_num}: {run_part(part_num, initial_data)} lights turned on after {NUM_ITER} iterations.')



if __name__ == '__main__':
    main(sys.argv[1])

