import numpy as np
import pandas as pd
import time

tic = time.time()


def read_data(file):
    with open(file) as raw_data:
        Instructions = raw_data.read()
        Instructions = Instructions.strip()
        Instructions = Instructions.split("\n")
        Instructions = [w.replace('turn off', '0,') for w in Instructions]
        Instructions = [w.replace('turn on', '1,') for w in Instructions]
        Instructions = [w.replace('toggle', '2,') for w in Instructions]
        Instructions = [w.replace('through', ',') for w in Instructions]
        Instructions = [w.split(",") for w in Instructions]
        Instructions = [[int(i) for i in w] for w in Instructions]
        return Instructions


matrix = np.zeros((1000, 1000))


def write_instructions(Instructions):
    if Instructions[0] == 1:
        matrix[Instructions[1]:(Instructions[3] + 1), Instructions[2]:(Instructions[4] + 1)] = matrix[Instructions[1]:(
                    Instructions[3] + 1), Instructions[2]:(Instructions[4] + 1)] + 1

    if Instructions[0] == 0:
        matrix[Instructions[1]:(Instructions[3] + 1), Instructions[2]:(Instructions[4] + 1)] = matrix[Instructions[1]:(
                    Instructions[3] + 1), Instructions[2]:(Instructions[4] + 1)] - 1

    if Instructions[0] == 2:
        matrix[Instructions[1]:(Instructions[3] + 1), Instructions[2]:(Instructions[4] + 1)] = matrix[Instructions[1]:(
                    Instructions[3] + 1), Instructions[2]:(Instructions[4] + 1)] + 2

    if Instructions[0] == 0:
        matrix[Instructions[1]:(Instructions[3] + 1), Instructions[2]:(Instructions[4] + 1)] = (matrix[Instructions[1]:(
                    Instructions[3] + 1), Instructions[2]:(Instructions[4] + 1)] + abs(
            matrix[Instructions[1]:(Instructions[3] + 1), Instructions[2]:(Instructions[4] + 1)])) / 2

    return matrix


def apply_instructions(Instructions):
    for s in Instructions:
        matrix_final = write_instructions(s)
    return matrix_final


def main():
    data = read_data("input.txt")
    print("Total brightness of lights is: {}".format(np.sum(apply_instructions(data))))


if __name__ == "__main__":
    main()
toc = time.time()
print("Part 2 time:" + str(1000 * (toc - tic)) + " ms")
