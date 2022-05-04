import time
import numpy as np


def parse(file_loc):
    """
    read input to list
    :param file_loc: file path to AOC Day2_input.txt
    returns array of arrays
    """
    values = []
    with open(file_loc, "r") as f:
        for l in f:
            values.append((l.strip().split("\t")))

    all_values = np.array(values).astype(int)

    return all_values


def get_even_dividers(list, sorted_values):
    """
    Given the list and sort list, using masking we get the even dividers and check that there are two remaining values
    :param list: The list of values to check
    :param sorted_values: The sorted list which will be the dividers
    :return: The result of the even division
    """
    for j in range(len(list)):
        even_dividers = list[list % sorted_values[j] == 0]
        if len(even_dividers) == 2:
            return (np.amax(even_dividers / sorted_values[j]))  # max used to select the correct value - not 1


def main(file_loc):
    full_list = parse(file_loc)

    # Part 1:
    difference = (np.amax(full_list, 1) - np.amin(full_list, 1))
    sum_difference = sum(difference)

    # Part 2:
    sum_dividers = 0
    # Sorting the list will try the smaller numbers as dividers first
    for i, val in enumerate(np.sort(full_list)):
        sum_dividers += (get_even_dividers(full_list[i], val))

    return sum_difference, sum_dividers


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'input.txt'

    sum_difference, sum_dividers = main(file_loc)
    print(f'Part 1: {sum_difference}')
    print(f'Part 2: {sum_dividers}')

    end_time = time.time()
    print(f'Time taken:{end_time - start_time}')
