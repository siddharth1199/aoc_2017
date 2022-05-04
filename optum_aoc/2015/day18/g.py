'''Day 18 Advent of Code, game of life'''

import sys
import time
import numpy as np

LEN = 100

def parse(file_loc, part_num):
    mygrid = np.zeros([LEN, LEN], dtype=int)
    with open(file_loc, "r") as myfile:
        for i, line in enumerate(myfile):
            grid_line = line.strip()
            for j, char in enumerate(grid_line):
                if char == '#':
                    mygrid[i, j] = 1
    if part_num == 2:
        mygrid[0, 0] = 1
        mygrid[0, -1] = 1
        mygrid[-1, 0] = 1
        mygrid[-1, -1] = 1
    halo_grid = np.zeros([LEN+2, LEN+2], dtype=int)
    halo_grid[1:-1, 1:-1] = mygrid
    return halo_grid


def count_neighbours(three_by_three):
    on_neighbours = np.sum(three_by_three) - three_by_three[1, 1]
    return on_neighbours


def single_step(initial, part_num):
    new = np.zeros_like(initial, dtype=int)
    for i in range(LEN):
        for j in range(LEN):
            num_on_neighbours = count_neighbours(initial[i:i+3, j:j+3])
            if initial[i+1, j+1] == 1:
                if num_on_neighbours == 2 or num_on_neighbours == 3:
                    new[i+1, j+1] = 1
            if initial[i+1, j+1] == 0:
                if num_on_neighbours == 3:
                    new[i+1, j+1] = 1
    if part_num == 2:
        new[1, 1] = 1
        new[1, -2] = 1
        new[-2, 1] = 1
        new[-2, -2] = 1
    return new


def animator(initial, num_steps, part_num):
    old = initial
    for _ in range(num_steps):  # specifying that I am not using the counter
        new = single_step(old, part_num)
        old = new
    return new


if __name__ == '__main__':
    start_time = time.time()
    input_file = 'input.txt'
    part = 2
    number_steps = 100

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
    if len(sys.argv) == 3:
        part = int(sys.argv[2])

    start_lights = parse(input_file, part)
    final = animator(start_lights, number_steps, part)
    lights_on = np.sum(final)
    print('The number of lights on at the end is {}'.format(lights_on))

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} seconds to execute'.format(duration))
