import sys


def read_input(file_name):
    with open(file_name) as file:
        lines = [int(d) for d in file.read().split('\t')]
    return lines


def solve_cycle(memory_banks):
    """
    What we do here is, append each unique tuple to a list which contains each combination, and check if the combo does
    exist after the redistribution of the max element.
    :param memory_banks:
    :return:
    """
    num_banks = len(memory_banks)
    combo_encountered = []
    while tuple(memory_banks) not in combo_encountered:  # Check if the combo is encountered before
        combo_encountered.append(tuple(memory_banks))  # Add current tuple to list
        current_max = max(memory_banks)  # Max value to distribute over other indexes
        max_index = memory_banks.index(current_max)  # Index of max value to distribute (note gives first index)
        memory_banks[max_index] = 0  # Set value of current_max index to be 0
        for i in range(current_max):
            next_index = (max_index + i + 1) % num_banks  # Distribute value over others in the loop
            memory_banks[next_index] += 1
    combo_encountered.append(tuple(memory_banks))  # Append value to list
    return len(combo_encountered) - 1, (len(combo_encountered) - 1) - combo_encountered.index(combo_encountered[-1])
    # Part 1: Simply the number of times we had to redistribute blocks,
    # (-1 done for the last time which is the duplicate combo)
    # Part 2: We get the difference in index of the org state vs when the state is seen again (towards the end)


def main(path):
    memory_banks = read_input(path)
    part1, part2 = solve_cycle(tuple(memory_banks))
    print(f'Part 1 = {part1} and part 2 = {part2}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])