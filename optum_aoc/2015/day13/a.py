import sys
import re
# This is just the Travelling Salesman Problem, which we've already solved!
sys.path.insert(0, '../day09/')  # Ugly but works - Bad decision of mine to break Python name chain with '2015' dir
from c import UndirectedGraph, held_karp


def parse(line: str):
    pattern = re.compile(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).')
    subject, sign, magnitude, target = re.match(pattern, line).groups()
    assert sign in ('gain', 'lose')
    value = int(magnitude) * (1 if sign == 'gain' else -1)
    return (subject, target), value


def main():
    relationships = UndirectedGraph()
    with open(sys.argv[1], 'r') as f:
        for line in f:
            relationships.increment_link(*parse(line))

    print(held_karp(relationships, compar=max))
    relationships['Host']  # Sneaky - Initialises host in relationships.keys()
    print(held_karp(relationships, compar=max))


if __name__ == '__main__':
    main()
