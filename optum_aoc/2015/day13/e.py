import re
import itertools


def load_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
        return [i.strip() for i in lines]


def parse_file(file):
    seating_arrangement = {}
    people = set()

    for line in file:
        line_re = re.compile(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).")
        person1, plus_minus, points, person2 = line_re.match(line).groups()

        if plus_minus == 'lose':
            points = -1 * int(points)
        else:
            points = int(points)

        seating_arrangement[person1 + person2] = seating_arrangement[person1 + person2] = points
        people.add(person1)
        people.add(person2)

    return seating_arrangement, people


def parse_part_two(file):
    seating_arrangement = {}
    people = set()

    for line in file:
        line_re = re.compile(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).")
        person1, plus_minus, points, person2 = line_re.match(line).groups()

        if plus_minus == 'lose':
            points = -1 * int(points)
        else:
            points = int(points)

        seating_arrangement[person1 + person2] = seating_arrangement[person1 + person2] = points

        people.add(person1)
        people.add(person2)

    for person in people:
        seating_arrangement[person + 'me'] = 0
        seating_arrangement['me' + person] = 0

    people.add('me')

    return seating_arrangement, people


def main(path):
    best = 0
    raw_file = load_file(path)
    seating_arrangement, people = parse_file(raw_file)
    #seating_arrangement, people = parse_part_two(raw_file)

    for route in itertools.permutations(people):
        happiness_points = 0

        for person_1, person_2 in zip(route, route[1:]):
            happiness_points += seating_arrangement[person_1 + person_2] + seating_arrangement[person_2 + person_1]

        happiness_points += seating_arrangement[route[-1] + route[0]] + seating_arrangement[route[0] + route[-1]]

        if happiness_points > best:
            best = happiness_points

    print("Best seating assignment:", route, best)


main('input.txt')