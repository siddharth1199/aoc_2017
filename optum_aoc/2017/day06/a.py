import time
import sys
import numpy as np
from copy import copy

"""
Note to reviewer
I used np.array() as that allowed me to use argmax() so I wouldnt have to loop over a list of numbers
to find the biggest memory bank, and also it allowed me to do vecotrised operations like self.block_distribution += 1 
which you cant do with python lists
however, this led to loads of problems as you cant do lots of things with np arrays
so I had to constantly convert lists to np.arrays and vice versa... not ideal, it may have been better just to use lists
and while loops... But if the memory banks were filled with millions of blocks instead of tens, my approach may be better?
"""


def parse(file_loc):
    """ parses input which is tab seperated, returns np array of integers """
    with open(file_loc, "r") as myfile:
        for line in myfile:
            list_strings = line.split('\t')
            list_ints = list(map(int, list_strings))
            np_array = np.array(list_ints)
    return np_array


class MemoryBanks:
    def __init__(self, block_distribution):
        self.block_distribution = block_distribution
        self.dict_of_previous_block_distributions = {0: list(copy(block_distribution))}  # otherwise the elements in list get updated as blocks get udpated, also we need to convert to list as we cant use if x in [] with x being an np.array
        self.number_banks = len(block_distribution)
        self.cycle_num = 0
        self.started_repeating = False
        return

    def redistribute_blocks(self):
        self.cycle_num += 1

        # find biggest bank, note in the event of a tie, the argamx function returns the lowest index value
        biggest_bank = self.block_distribution.argmax()

        # avoid loop by computing number of extra blocks for all and for some by divmod
        num_blocks_for_all, remainder = divmod(self.block_distribution[biggest_bank], self.number_banks)

        # create new memory bank array
        self.block_distribution[biggest_bank] = 0
        self.block_distribution += num_blocks_for_all
        if remainder + biggest_bank + 1 > self.number_banks:
            # need to wrap with indexing, easier to find ones that dont go up, put them all up 1, then bring those down
            number_mising = self.number_banks - remainder
            self.block_distribution += 1
            self.block_distribution[biggest_bank+1-number_mising:biggest_bank+1] -= 1
        else:
            self.block_distribution[biggest_bank+1:biggest_bank+1+remainder] += 1

        # check if found repeated configuraiton
        if list(self.block_distribution) in self.dict_of_previous_block_distributions.values():
            self.started_repeating = True
        # add new configuration to set of previous ones
        self.dict_of_previous_block_distributions[self.cycle_num] = list(copy(self.block_distribution))
        return None


def main(file_loc):
    inputs = parse(file_loc)

    memory_instance = MemoryBanks(inputs)
    while not memory_instance.started_repeating:
        memory_instance.redistribute_blocks()
        #print(memory_instance.cycle_num)
        #print(memory_instance.block_distribution)
        #print(memory_instance.list_of_previous_block_distributions)

    repeated_config = list(memory_instance.block_distribution)
    repeated_cycle_numbers = [key for key, value in memory_instance.dict_of_previous_block_distributions.items()
                              if value == repeated_config]
    repeat_frequency = repeated_cycle_numbers[1] - repeated_cycle_numbers[0]

    return memory_instance.cycle_num, repeat_frequency


if __name__ == '__main__':
    start_time = time.time()
    input_file = 'day06_input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

    answer_part_1, answer_part_2 = main(input_file)
    print('the solution to part a and b are {} and {}'.format(answer_part_1, answer_part_2))

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} milliseconds to execute'.format(1000*duration))