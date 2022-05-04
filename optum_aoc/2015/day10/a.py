import sys
import numpy as np

# import array as arr

''' Increase this if running into out of bounds ERROR '''
MAX_LEN = 10000000


def generate_string(input_arr, result_len):
    ''' Native array is much slower than numpy array '''
    result = np.full(shape=MAX_LEN, fill_value=0, dtype=np.uint8)
    # result = arr.array("B", [0] * MAX_LEN)

    curr_char = input_arr[0]
    curr_len = 1
    curr_idx = 0
    for i in range(1, result_len):
        c = input_arr[i]
        if c != curr_char:
            result[curr_idx] = curr_len
            result[curr_idx + 1] = curr_char
            curr_idx += 2
            curr_len = 1
            curr_char = c
        else:
            curr_len += 1
    result[curr_idx] = curr_len
    result[curr_idx + 1] = curr_char

    return tuple([result, (curr_idx + 2)])


def solve(input_str):
    result = np.full(shape=MAX_LEN, fill_value=0, dtype=np.uint8)
    # result = arr.array("B", [0] * MAX_LEN)

    for i in range(len(input_str)):
        result[i] = int(input_str[i])
    result_len = len(input_str)

    for i in range(40):
        result, result_len = generate_string(result, result_len)
    part_one = result_len
    for i in range(10):
        result, result_len = generate_string(result, result_len)

    return tuple([part_one, result_len])


if __name__ == "__main__":
    #input_str = '1321131112'

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            input_str = f.readline().strip()

    answers = solve(input_str)

    print('Part One: ' + str(answers[0]))
    print('Part Two: ' + str(answers[1]))