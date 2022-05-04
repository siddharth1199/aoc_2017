from typing import List, Tuple
from operator import add
from itertools import accumulate

# Unashamedly stolen and adapted from Peter Norvig's Pytudes 2020
def data(day: int, parser=str, sep='\n') -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    with open(f"input.txt") as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))


# representing a step in either X or Y coordinates
Direction = Tuple[int, int]
Coordinate = Tuple[int, int]


def parse_direction(line: str) -> List[Direction]:
    "Parse arrows into Directions"
    arrow_lookup = {
        "^": (0, 1),
        ">": (1, 0),
        "v": (0, -1),
        "<": (-1, 0)
    }
    return [arrow_lookup[arrow] for arrow in line]


def next_coord(coordinate: Coordinate, direction: Direction) -> Coordinate:
    "Given current coordinate and next direction return next coordinate"
    return tuple(map(add, coordinate, direction))


def split_directions(directions: List[Direction]) -> Tuple[List[Direction], List[Direction]]:
    "Split a list of directions into two lists of directions"
    santa, robosanta = [], []
    for i, direction in enumerate(directions):
        if i % 2 == 0:
            santa.append(direction)
        else:
            robosanta.append(direction)
    return (santa, robosanta)


if __name__ == "__main__":
    start_coord = (0, 0)
    directions = data(3, parse_direction)[0]
    coords = list(accumulate(directions, next_coord, initial=start_coord))

    print(f"Part 1: {len(set(coords))}")

    santa_directions, robo_directions = split_directions(directions)
    santa_coords = list(accumulate(santa_directions, next_coord, initial=start_coord))
    robo_coords = list(accumulate(robo_directions, next_coord, initial=start_coord))

    print(f"Part 2: {len(set(santa_coords + robo_coords))}")
