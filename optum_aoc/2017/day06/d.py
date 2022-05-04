import time

def parse(file_loc):
    """ read input to list """
    inputs = open(file_loc, "r").read().split('\t')
    int_input = [int(x) for x in inputs]

    return int_input


def redistribute(memory_banks, double_index):
    """
    This function finds the bank with highest number of bytes and redistributes them to other banks
    """
    blocks_to_redist = max(memory_banks)
    biggest_bank = memory_banks.index(blocks_to_redist)

    memory_banks[biggest_bank]=0
    to_increase = double_index[biggest_bank + 1: biggest_bank + blocks_to_redist+1]

    for i in to_increase:
        memory_banks[i]+=1

    return memory_banks


def reallocation(initial_memory_banks):
    """
    This function calls the redistribute function and checks if the bank values have been seen before
    """
    distributions =[]

    # Double the index so we can iterate through easily
    double_index = list(range(0,len(initial_memory_banks),1))+list(range(0,len(initial_memory_banks),1))

    new_banks = redistribute(initial_memory_banks, double_index)

    while new_banks not in distributions:

        distributions.append(new_banks.copy())
        new_banks = redistribute(new_banks, double_index)

    return len(distributions)+1, distributions.index(new_banks)


def main(file_loc):

    initial_memory_banks = parse(file_loc)
    part1, previous_entry = reallocation(initial_memory_banks)
    part2 = part1-previous_entry-1

    print(f'Answer to part 1: {part1}')
    print(f'Answer to part 2: {part2}')


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'Day6_input.txt'

    main(file_loc)

    end_time = time.time()
    print(f'Time taken:{(end_time - start_time)*1000} miliseconds')