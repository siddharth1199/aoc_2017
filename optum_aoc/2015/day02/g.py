from typing import List, Tuple
from operator import add
from itertools import accumulate

# Unashamedly stolen and adapted from Peter Norvig's Pytudes 2020
def data(day: int, parser=str, sep='\n') -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    with open(f'input.txt') as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))

def first(iterable, predicate, default = None):
    """
    Return the first item in `iterable` that satisfies `predicate` or 
    return `default` if no item satisfies `predicate`.
    """
    return next((x for x in iterable if predicate(x)), default)

def first_pos(iterable, predicate, default = None):
    """
    Return a tuple of the first index and item `(i, x)` in `iterable` that satisfies 
    `predicate` or `default` if no item satisfies `predicate`. 
    """
    return next(((i, x) for i, x in enumerate(iterable) if predicate(x)), (None, default))


Measurement = Tuple[int, int, int]
Area = int
Length = int

def parse_measurement(line: str) -> Measurement:
    l, w, h = line.split("x")
    return int(l), int(w), int(h)

def surface_area(m: Measurement) -> Area:
    l, w, h = m
    return 2*l*w + 2*w*h + 2*h*l

def smallest_side(m: Measurement) -> Area:
    s1, s2, _ = sorted(m)
    return s1 * s2

def total_wrapping(m: Measurement) -> Area:
    return surface_area(m) + smallest_side(m)

def ribbon_length(m: Measurement) -> Length:
    s1, s2, _ = sorted(m)
    return 2*s1 + 2*s2

def bow_length(m: Measurement) -> Length:
    l, w, h = m
    return l * w * h

def total_ribbon(m: Measurement) -> Length:
    return ribbon_length(m) + bow_length(m)

if __name__ == "__main__":
    measurements = data(2, parse_measurement)
    print(f"Total wrapping paper: {sum(total_wrapping(m) for m in measurements)}")
    print(f"Total ribbon: {sum(total_ribbon(m) for m in measurements)}")
    