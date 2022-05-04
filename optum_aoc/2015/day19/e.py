import collections
import string


def parse(path='input.txt'):
    replacements = collections.defaultdict(list)
    with open(path) as f:
        for line in f:
            if '=' in line:
                tokens = line.split()
                from_char, to_char = tokens[0], tokens[-1]
                replacements[from_char].append(to_char)
            else:
                molecule = line.strip()
    return replacements, molecule


def parse_molecule(molecule_str):
    element_lst = []
    upper_letters = set(string.ascii_uppercase)
    prev = None
    for s in molecule_str:
        if s in upper_letters or s == 'e':
            if prev is not None:
                element_lst.append(prev)
            prev = s
            if s == 'e':
                element_lst.append(s)
                prev = None
        else:
            element_lst.append(prev + s)
            prev = None
    if prev is not None:
        element_lst.append(prev)
    return element_lst


def main():
    replacements, molecule = parse()
    molecule_set = set()
    element_lst = parse_molecule(molecule)
    for idx, s in enumerate(element_lst):
        for replacement in replacements[s]:
            molecule_set.add(''.join(element_lst[:idx] + [replacement] + element_lst[idx + 1:]))
    print('Answer for part 1: {}'.format(len(molecule_set)))


if __name__ == '__main__':
    main()