import sys
import re

REPLACEMENT_RULES = dict()


def read_input(fname):
    with open(fname, 'r') as f:
        for line in f:
            m = re.search(r'(.*) => (.*)', line)
            if m:
                elements = m.groups()
                REPLACEMENT_RULES.setdefault(elements[0], []).append(elements[1])
            elif len(line) > 1:
                return line.strip()


def find_distinct_replacements(molecule):
    molecules = set()
    elements = re.findall('[A-Z][^A-Z]*', molecule)

    for i, element in enumerate(elements):
        new_elements = elements.copy()
        replacements = REPLACEMENT_RULES.get(element, [element])
        for replacement in replacements:
            new_elements[i] = replacement
            molecules.add(''.join(new_elements))

    # In case original molecule is added to the set - this results from the above code when there is no replacement for a certain element
    molecules.remove(molecule)
    return molecules


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 1

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    print(len(find_distinct_replacements(read_input(input_file))))