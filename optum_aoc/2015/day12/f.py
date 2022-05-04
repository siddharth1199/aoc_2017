import sys
import ast

NUMERIC_LIST = []

def load_input(fname):
    with open(fname, "r") as f:
        file = f.read()
        file = ast.literal_eval(file)
        return file


def check_type(i, red_pass):

        if isinstance(i, list):
            for j in i:
                check_type(j, red_pass)

        elif isinstance(i, dict):
            dict_values = i.values()
            if red_pass:
                for j in dict_values:
                    check_type(j, red_pass)
            else:
                if not "red" in dict_values:
                    for j in dict_values:
                        check_type(j, red_pass)

        if isinstance(i, int):
            NUMERIC_LIST.append(i)


def main(puzzle_input, red_pass):
    file = load_input(puzzle_input)
    if isinstance(file, list):
        for i in file:
            check_type(i, red_pass)
    elif isinstance(file, dict):
        for i in file.values():
            check_type(i, red_pass)
    print('Total of all numeric elements: {}'.format(sum(NUMERIC_LIST)))


if __name__ == "__main__":
    if len(sys.argv) ==1:
        print("USAGE: python [script.py] [puzzle_input] [part_num]")
        puzzle_input = "day_12.txt"

    if len(sys.argv) > 1:
        puzzle_input = sys.argv[1]

    if len(sys.argv) > 2:
        part_num = sys.argv[2]
    else:
        part_num = '1'
        print('Defaulting to part 1')

    red_pass = True if part_num == '1' else False
    main(puzzle_input, red_pass)
