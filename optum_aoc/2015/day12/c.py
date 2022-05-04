import sys
import json


def get_ints(thing, to_skip=''):
    """
    The original problem input is a dict.
    Each value of the dict is either another dict, a list, a string, or an int.
    This is true recursively, so to speak.

    For each thing we see,
     * if it's an int, return it (or yield it, rather)
     * if it's a string, do nothing
     * if it's a list, apply get_ints to each of its elements
     * if it's a dict, apply get_ints to each of its values IF
       none of its values are the thing we want to skip

    This is another time where pattern matching can be handy.
    """
    if isinstance(thing, int):
        yield thing
    elif isinstance(thing, dict):
        values = thing.values()
        if to_skip not in values:
            for value in values:
                yield from get_ints(value, to_skip)
    elif isinstance(thing, list):
        for entry in thing:
            yield from get_ints(entry, to_skip)
    elif isinstance(thing, str):
        pass
    else:
        print(f'You made a mistake: {thing}, {type(thing)}')


def main(input_path):

    with open(input_path, 'r') as f:
        data = json.load(f)

    part1 = sum(get_ints(data))
    part2 = sum(get_ints(data, to_skip='red'))

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main(sys.argv[1])

