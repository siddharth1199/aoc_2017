import time
import sys


def parse(file_loc):
    """ parses input which in this case is a single line of digits
    returns input: a string """
    instruction_list = []
    with open(file_loc, "r") as myfile:
        for line in myfile:
            instruction_list.append(int(line.strip()))
    return instruction_list


def one_step(current_loc, current_list, part):
    """ move to the next location, update value of previous location
    this is a subroutine, the list is modified without returning the list """
    new_loc = current_loc + current_list[current_loc]
    if (part == 2) and (current_list[current_loc] >= 3):
        current_list[current_loc] -= 1
    else:
        current_list[current_loc] += 1
    return new_loc


def run_list(orders, part):
    steps_executed = 0
    current_position = 0
    len_list = len(orders)
    while current_position < len_list:
        steps_executed += 1
        current_position = one_step(current_position, orders, part)
    return steps_executed


def main(file_loc):
    orders = parse(file_loc)
    answer_part_1 = run_list(orders, 1)

    orders2 = parse(file_loc)
    answer_part_2 = run_list(orders2, 2)
    return answer_part_1, answer_part_2


if __name__ == '__main__':
    start_time = time.time()
    input_file = 'day05_input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

    answer_part_1, answer_part_2 = main(input_file)
    print('the solution to part a and b are {} and {}'.format(answer_part_1, answer_part_2))

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} milliseconds to execute'.format(1000*duration))