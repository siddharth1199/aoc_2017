import re
import collections
from copy import deepcopy
import sys

mol_match_dict = collections.defaultdict(list)


def parse_input(file):
    with open(file, "r") as f:
        for line in f:
            if re.search(r'(.*) => (.*)', line):
                element, option = re.match(r'(.*) => (.*)', line).groups()
                mol_match_dict[element].append(option)
            else:
                molecule = line
    return molecule, mol_match_dict


def main(file):
    molecule, mol_match_dict = parse_input(file)
    regex_pat = r"({})".format("|".join(re.escape(s) for s in mol_match_dict.keys()))
    split_mol = re.split(regex_pat, molecule)
    only_mol = [x for x in split_mol if x]
    list_new_mol = []

    for pos, i in enumerate(only_mol):
        new_list = deepcopy(only_mol)
        for j in mol_match_dict[i]:
            new_list[pos] = j
            list_new_mol.append("".join(new_list))
    print(f'The number of unique new molecules created for input after 1 step: {len(set(list_new_mol))}')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("USAGE: python [script.py] [input.txt]")
    if len(sys.argv) > 1:
        puzzle_input = sys.argv[1]
    else:
        puzzle_input = 'input.txt'
    main(puzzle_input)