''' Quiet possibly slower than simulation solutions - just submitted to compare the performance! '''

import numpy as np
import sys


def load_input(fname):
    parameters = []
    with open(fname, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            tokens = line.split()
            parameters.append((int(tokens[3]), int(tokens[6]), int(tokens[6]) + int(tokens[-2]), 0, 0))

    return np.array(parameters, dtype=[('speed', '<i4'), ('fl_len', '<i4'), ('cycle_len', '<i4'), ('fl_dist', '<i4'),
                                       ('score', '<i4')])


def calculate_scores(parameters, race_len):
    for i in range(parameters.shape[0]):
        time_left = race_len % (parameters['cycle_len'][i])
        parameters['fl_dist'][i] = (min(time_left, parameters['fl_len'][i]) + int(
            race_len / parameters['cycle_len'][i]) * parameters['fl_len'][i]) * parameters['speed'][i]

    winners = np.argwhere(parameters['fl_dist'] == parameters['fl_dist'].max()).flatten().tolist()
    parameters['score'][winners] += 1

    return parameters


def solve(fname, race_len, part_num):
    parameters = load_input(fname)
    if part_num == 1:
        parameters = calculate_scores(parameters, race_len)
        return max(parameters['fl_dist'])
    elif part_num == 2:
        for sec in range(race_len):
            parameters = calculate_scores(parameters, sec)
        return max(parameters['score']) - 1


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 2

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    print(solve(input_file, 2503, part_num))

