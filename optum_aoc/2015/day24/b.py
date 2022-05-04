""" Day 24 Advent of Code, balancing
The code now runs in 4 minutes as I added early stopping, it could still be more effficient for reasons
explained below
"""

import sys
import time
import numpy as np
from itertools import combinations
from copy import deepcopy


def parse(file_loc):
    """ creates list of parcel weights """
    parcel_weights = []
    with open(file_loc, "r") as myfile:
        for line in myfile:
            parcel_weights.append(int(line.strip()))
    return parcel_weights


def single_group_creator(parcel_weights):
    """generator that makes tuple of all possible combinations that could be in a group"""
    for r in range(1, len(parcel_weights)):
        group_1 = combinations(parcel_weights, r)  # this is a generator
        yield from group_1


def three_groups_creator(parcel_weights):
    """ generator that makes list of three tuples with equal sums by exhaustive search
    ie this only returns combos that meet santas criteria, it returns them in sorted order
    so that first returned have lowest number in front group """
    total_weight = sum(parcel_weights)
    assert(total_weight % 3 == 0), 'weight cannot be split into 3 equal groups'
    target_weight = total_weight / 3

    first_group_gen = single_group_creator(parcel_weights)  # this generator is only called once

    for first_group in first_group_gen:
        if sum(first_group) == target_weight:
            remaining_after_one_presents = deepcopy(parcel_weights)
            for present in first_group:
                remaining_after_one_presents.remove(present)

            second_group_gen = single_group_creator(remaining_after_one_presents) # this generator is called many times
            for second_group in second_group_gen:
                if sum(second_group) == target_weight:
                    remaining_after_two_presents = deepcopy(remaining_after_one_presents)
                    for present_2 in second_group:
                        remaining_after_two_presents.remove(present_2)
                    third_group = tuple(remaining_after_two_presents)
                    yield [first_group, second_group, third_group]


def brute_force(parcel_weights):
    """ there are more than 28 billion combinations so this is probably not a good approach
    but I have it printing out the current best arrangment every million iterations
    and if you enter the current best to Advent of Code it is right, so this works, even though
    I have never seen my code finish """
    i = 0
    combo_generator = three_groups_creator(parcel_weights)  # generator of combos that meet santas requirements

    best_num_front = 100
    best_quantum = 1000000000
    best_combo = []

    # my code is inefficient as after finding a combination that works, it checks for different combinations which
    # have the same first group but regarrangments of the 2nd and 3rd groups. I need to tell my code to stop doing this
    # as dont care about the 2nd and 3rd groups as long as they have equal weights.
    # eg [(1, 83, 103, 107, 109, 113), (3, 17, 59, 71, 79, 89, 97, 101), (5, 11, 13, 19, 23, 29, 31, 41, 43, 47, 53, 61, 67, 73)]
    # eg [(1, 83, 103, 107, 109, 113), (3, 71, 79, 89, 97, 101), (5, 11, 13, 17, 59, 19, 23, 29, 31, 41, 43, 47, 53, 61, 67, 73)]

    # need to stop asking for new combos when the current combo group 1 is bigger than best sol group 1
    lenght_last_combo_first_group = 0
    while lenght_last_combo_first_group <= best_num_front:
        combo = next(combo_generator)
        # checking progress, note the counter here is just of valid combinations where sum == target_weight, not
        # of all possible combinations which are many times greater
        lenght_last_combo_first_group = len(combo[0])
        i += 1
        if i % 100000 == 0:
            print(f'checking valid combination {i}, which has {len(combo[0])} presents in the front, so far the best solution has {best_num_front} presents in the front'
                  f' and has a quantum entanglement of {best_quantum}')
            print(best_combo)

        # brute force solution
        if len(combo[0]) == best_num_front:
            quantum_tangle = np.prod(combo[0])
            if quantum_tangle < best_quantum:
                best_quantum = quantum_tangle
                best_combo = combo
        elif len(combo[0]) < best_num_front:
            best_num_front = len(combo[0])
            best_quantum = np.prod(combo[0])
            best_combo = combo

    return best_combo, best_num_front, best_quantum


if __name__ == '__main__':
    start_time = time.time()
    input_file = 'input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

    presents = parse(input_file)
    optimum_combo, num_front, quantum_value = brute_force(presents)

    print(f'the final solution is {optimum_combo}, with just {num_front} presents in the front'
          f' and a quantum entanglement of {quantum_value}')

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} seconds to execute'.format(duration))
