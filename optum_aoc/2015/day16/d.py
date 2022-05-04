import sys

COMP_REFERENCE = {'children': 3,
                  'cats': 7,
                  'samoyeds': 2,
                  'pomeranians': 3,
                  'akitas': 0,
                  'vizslas': 0,
                  'goldfish': 5,
                  'trees': 3,
                  'cars': 2,
                  'perfumes': 1}
GREATER_KEYS = ('cats', 'trees')
FEWER_KEYS = ('pomeranians', 'goldfish')
EQUAL_KEYS = tuple(list(COMP_REFERENCE.keys() - set(FEWER_KEYS + GREATER_KEYS)))


def find_aunt(fname, part_num):
    def update_values(values, tokens):
        values[tokens[2][:-1]] = int(tokens[3][:-1])
        values[tokens[4][:-1]] = int(tokens[5][:-1])
        values[tokens[6][:-1]] = int(tokens[7])

    with open(fname, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            tokens = line.split()

            line_compounds = COMP_REFERENCE.copy()

            if part_num == 1:
                update_values(line_compounds, tokens)

                if line_compounds == COMP_REFERENCE:
                    print(tokens[1][:-1])
                    break

            elif part_num == 2:
                # To handle inequalities of unknown compounds
                line_compounds['cats'] += 1
                line_compounds['trees'] += 1
                line_compounds['pomeranians'] -= 1
                line_compounds['goldfish'] -= 1

                update_values(line_compounds, tokens)

                if all([line_compounds[key] > COMP_REFERENCE[key] for key in GREATER_KEYS]) & \
                        all([line_compounds[key] < COMP_REFERENCE[key] for key in FEWER_KEYS]) & \
                        all([line_compounds[key] == COMP_REFERENCE[key] for key in EQUAL_KEYS]):
                    print(tokens[1][:-1])
                    break


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 2

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    find_aunt(input_file, part_num)
