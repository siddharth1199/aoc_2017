import time

def parse(file_loc):
    """
    read input to list
    :param file_loc: file path to AOC Day5_input.txt
    """
    input_strings = open(file_loc, "r").read().split('\n')
    input = [int(x) for x in input_strings]

    return input


def taking_a_step(index, list, part):
    """
    takes a step by incrementing the index and getting the new value
    """
    next_index = index + list[index]

    if part == 2:
        if list[index] > 2:
            list[index] -= 1
        else:
            list[index] += 1
    else:
        list[index] += 1
    return next_index, list


def looping_through_steps(steps_list, part):
    """
    loop through the steps until we have exited the list
    """
    current_index = 0
    steps = 0

    while len(steps_list) > current_index > -1:
        current_index, steps_list = taking_a_step(current_index, steps_list, part)
        steps+=1

    return steps


def main(file_loc):

    full_list = parse(file_loc)
    full_list2 = full_list.copy() # needed to copy list to use in part 2 

    answer_1 = looping_through_steps(full_list, 1)
    answer_2 = looping_through_steps(full_list2, 2)

    print(f'The answer to part 1 is: {answer_1}')
    print(f'The answer to part 1 is: {answer_2}')

    return None


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'Day5_input.txt'

    main(file_loc)

    end_time = time.time()
    print(f'Time taken:{(end_time - start_time)*1000} miliseconds')