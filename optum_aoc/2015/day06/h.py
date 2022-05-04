import re
import sys
import numpy as np

light_grid = np.zeros((1000, 1000), dtype=np.int8)

# List of instructions for both parts of the problem
instructions = [{'turn on': lambda x: 1,
                 'turn off': lambda x: 0,
                 'toggle': lambda x: 1 - x},
                {'turn on': lambda x: x + 1,
                 'turn off': lambda x: np.maximum(0, x - 1),
                 'toggle': lambda x: x + 2}]


def run_instructions(fname, part_num):
    with open(fname, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            instruction, *indices = re.search('(\w*\s*\w*)\s([0-9]*),([0-9]*) through ([0-9]*),([0-9]*)', line).groups()
            indices = list(map(int, indices))

            # Call the corresponding function to the instruction
            op = instructions[part_num - 1][instruction]
            new_block = op(light_grid[indices[0]:indices[2] + 1, indices[1]:indices[3] + 1])

            light_grid[indices[0]:indices[2] + 1, indices[1]:indices[3] + 1] = new_block
    return


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 2
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    run_instructions(input_file, part_num)

    print(np.sum(light_grid))
