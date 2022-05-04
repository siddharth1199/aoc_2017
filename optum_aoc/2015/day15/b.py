import numpy as np
import sys


def read_input(fname):
    data_rows = []
    with open(fname, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            tokens = line.split()
            data_rows.append(
                [int(tokens[2][:-1]), int(tokens[4][:-1]), int(tokens[6][:-1]), int(tokens[8][:-1]), int(tokens[-1])])

    return np.transpose(np.array(data_rows))


# Brute force for now...
def solve(weights):
    max_score = -np.Inf
    max_values = np.zeros((4, 1))
    max_perc = np.zeros((4, 1))
    for i in range(1, 100 - 3):
        for j in range(1, (100 - 2 - i)):
            for k in range(1, (100 - 1 - i - j)):
                l = 100 - i - j - k
                values = np.maximum(0, np.matmul(weights[:-1, :], np.array([i, j, k, l])))
                prod_val = np.prod(values)
                if prod_val > max_score:
                    max_score = prod_val
                    max_values = values
                    max_perc = np.array([i, j, k, l])
    return max_score, max_perc, max_values


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 1

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    weights = read_input(input_file)

    max_score, _, _ = solve(weights)
    print(max_score)
