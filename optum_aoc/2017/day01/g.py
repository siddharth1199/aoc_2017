import time

def parse(file_loc):
    """
    read input to list
    :param file_loc: file path to AOC Day1_input.txt
    """
    values = []
    input = open(file_loc, "r").read().strip('\n')

    values.append([int(v) for line in input for v in line])

    return values[0]

def main(file_loc, part):

    assert(part in [1, 2]), 'Please select part 1 or 2'

    full_list = parse(file_loc)

    # change the indexes of original list to use in comparison
    if part == 1:
        # push index of each item out one
        pushed_list = full_list[-1:] + full_list[:-1]
    else:
        # split list in half and make second half the first half
        half = int(len(full_list)/2)
        pushed_list = full_list[half:] + full_list[:half]

    # check if values in two lists are equal and sum
    same_values = [i for i, j in zip(full_list, pushed_list) if i==j]

    total_sum = sum(same_values)

    return total_sum

if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'Day1_input.txt'

    part = 2

    answer = main(file_loc, part)
    print(f'The sum is {answer}')

    end_time = time.time()
    print(f'Time taken:{end_time - start_time}')