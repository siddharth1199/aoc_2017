""" Day 24 Advent of Code, balancing
The code now runs in 2 minutes as I added early stopping, it could still be more effficient for reasons
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


def group_checker(proposed_group, target_weight, remaining_parcel_weights):
    """ checks if proposed group meets criteria,
    if so removes the presents of this group from list of remaining presents"""
    if sum(proposed_group) == target_weight:
        remaining_after_new_group_removed = deepcopy(remaining_parcel_weights)
        for present in proposed_group:
            remaining_after_new_group_removed.remove(present)
        return True, remaining_after_new_group_removed
    else:
        return False, None


def four_groups_creator(parcel_weights):
    """ generator that makes list of four tuples with equal sums by exhaustive search"""
    total_weight = sum(parcel_weights)
    assert(total_weight % 4 == 0), 'weight cannot be split into 4 equal groups'
    target_weight = total_weight / 4

    first_group_gen = single_group_creator(parcel_weights)  # this generator is only called once
    for first_group in first_group_gen:
        criteria_one, remaining_after_one_presents = group_checker(first_group, target_weight, parcel_weights)
        if criteria_one:

            second_group_gen = single_group_creator(remaining_after_one_presents)  # this generator is called many times
            for second_group in second_group_gen:
                criteria_two, remaining_after_two_presents = group_checker(second_group, target_weight, remaining_after_one_presents)
                if criteria_two:

                    third_group_gen = single_group_creator(remaining_after_two_presents)  # this generator is called many times
                    for third_group in third_group_gen:
                        criteria_three, remaining_after_three_presents = group_checker(third_group, target_weight, remaining_after_two_presents)
                        if criteria_three:

                            fourth_group = tuple(remaining_after_three_presents)

                            yield [first_group, second_group, third_group, fourth_group]


def brute_force(parcel_weights):
    """ checks all possible correct solutions, starting with those with lowest number in front,
    hence allowing early stopping, but code is still inefficient for reasons explained below """
    i = 0
    combo_generator = four_groups_creator(parcel_weights)

    best_num_front = 100
    best_quantum = 1000000000
    best_combo = []

    # my code is inefficient as after finding a combination that works, it checks for different combinations which
    # have the same first group but regarrangments of the 2nd, 3rd and 4th groups. I need to tell my code to stop doing this
    # as dont care about the 2nd, 3rd and 4th groups as long as they have equal weights.
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
        if i % 1000000 == 0:
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
    input_file = 'Day24_input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

    presents = parse(input_file)
    optimum_combo, num_front, quantum_value = brute_force(presents)

    print(f'the final solution is {optimum_combo}, with just {num_front} presents in the front'
          f' and a quantum entanglement of {quantum_value}')

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} seconds to execute'.format(duration))
