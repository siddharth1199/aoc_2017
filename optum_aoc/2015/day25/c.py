""" Day 25 Advent of Code, diaganol stuff """

import sys
import time
import re
import numpy as np


INITIAL_VALUE = 20151125
MULTIPLY = 252533
DIVIDE = 33554393


def parse(file_loc):
    """ returns target row and column number """
    pattern = r'(\d+)'
    with open(file_loc, "r") as myfile:
        for line in myfile:
            regex_matches = re.findall(pattern, line)
    row = int(regex_matches[0])
    column = int(regex_matches[1])
    return row, column


def next_code(old_code):
    """ computes value of next code"""
    product = old_code * MULTIPLY
    remainder = product % DIVIDE
    return remainder


def dynamic_fill(grid, previous_value):
    """ fills up top left half of grid, note this is sub routine, it acts on original input """
    grid_length = grid.shape[0]

    for i in range(1, grid_length):
        for j in range(i+1):
            grid[i-j, j] = next_code(previous_value)
            previous_value = grid[i-j, j]

    return None


if __name__ == '__main__':
    start_time = time.time()
    input_file = 'input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

    row_num, col_num = parse(input_file)

    # Initilise code_grid
    max_grid_size = row_num + col_num
    code_grid = np.zeros([max_grid_size, max_grid_size])
    code_grid[0, 0] = INITIAL_VALUE

    # Fill grid
    dynamic_fill(code_grid, INITIAL_VALUE)

    solution = code_grid[row_num-1, col_num-1]  # offset for python indexing starting at 0
    print(f'the code is {solution}')

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} seconds to execute'.format(duration))
