import time
import sys
import numpy as np


def parse(file_loc):
    """ returns input as np array """
    list_of_lists = []
    with open(file_loc, "r") as myfile:
        for line in myfile:
            row = line.strip()
            row_as_list_str = list(row)
            row_as_list_int = list(map(int, row_as_list_str))
            list_of_lists.append(row_as_list_int)
    return np.array(list_of_lists)


def find_low_points(np_input):
    # note being equal to adjacent point is not sufficient, must be lower

    # make array with boarder of 9s
    num_rows, num_cols = np_input.shape
    input_with_halo = np.ones((num_rows+2, num_cols+2))*9
    input_with_halo[1:-1, 1:-1] = np_input

    # for every point in matrix check if point above/below/left/right is lower
    lower_than_above = np_input < input_with_halo[0:-2, 1:-1]
    lower_than_below = np_input < input_with_halo[2:, 1:-1]
    lower_than_left = np_input < input_with_halo[1:-1, 0:-2]
    lower_than_right = np_input < input_with_halo[1:-1, 2:]

    lowest_point = lower_than_above & lower_than_below & lower_than_left & lower_than_right
    return lowest_point


def find_basins(np_input):
    # the 9s mark the barriers between basins
    np_nines = np_input >= 9

    # how to find which basin a point belongs to ??
    return 'something'


def main(file_loc):
    """ reads input and ?? """
    np_input = parse(file_loc)

    low_points = find_low_points(np_input)
    risk_score = np_input * low_points
    total_risk = risk_score.sum() + low_points.sum()

    basins = find_basins(np_input)

    return total_risk, basins


if __name__ == '__main__':
    start_time = time.time()
    input_file = 'day09_input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

    answer_a, answer_b = main(input_file)
    print('the solution to part a and b are {} and {}'.format(answer_a, answer_b))

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} milliseconds to execute'.format(1000*duration))