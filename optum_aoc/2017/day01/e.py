import time
import sys


def parse(file_loc):
    """ parses input which in this case is a single line of digits
    returns input: a string """
    with open(file_loc, "r") as myfile:
        for line in myfile:
            input = line.strip()
    return input


def part_1(input):
    answer = 0
    for i in range(len(input)-1): # dont include last digit in loop
        if input[i] == input[i+1]:
            answer += int(input[i])
    # do last digit here
    if input[0] == input[-1]:
        answer += int(input[0])
    return answer


def part_2(input):
    answer = 0
    lenght = len(input)
    offset_input = input[int(lenght/2):] + input[0:int(lenght/2)]
    for x, y in zip(input, offset_input):
        if x == y:
            answer += int(x)
    return answer


def main(file_loc):
    input = parse(file_loc)
    answer_part_1 = part_1(input)
    answer_part_2 = part_2(input)
    return answer_part_1, answer_part_2


if __name__ == '__main__':
    start_time = time.time()
    input_file = 'day01_input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

    answer_part_1, answer_part_2 = main(input_file)
    print('the solution to part a and b are {} and {}'.format(answer_part_1, answer_part_2))

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} milliseconds to execute'.format(1000*duration))