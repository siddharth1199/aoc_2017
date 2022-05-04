from typing import Callable, Tuple, List
import re
import numpy as np 

Grid = np.ndarray
Coord = Tuple[int, int]
Instruction = Tuple[Callable, Coord, Coord]


def turn_on(grid: Grid, x: Coord, y: Coord, part: bool) -> Grid:
    if part:
        grid[x[0]:y[0]+1, x[1]:y[1]+1] = 1
    else:
        grid[x[0]:y[0]+1, x[1]:y[1]+1] += 1
    return grid


def turn_off(grid: Grid, x: Coord, y: Coord, part: bool) -> Grid:
    if part:
        grid[x[0]:y[0]+1, x[1]:y[1]+1] = 0
    else:
        grid[x[0]:y[0]+1, x[1]:y[1]+1] = np.maximum(0, grid[x[0]:y[0]+1, x[1]:y[1]+1] - 1)
    return grid


def toggle(grid: Grid, x: Coord, y: Coord, part: bool) -> Grid:
    if part:
        grid[x[0]:y[0]+1, x[1]:y[1]+1] = 1 - grid[x[0]:y[0]+1, x[1]:y[1]+1]
    else:
        grid[x[0]:y[0]+1, x[1]:y[1]+1] += 2
    return grid


def parse_instructions(inst: str) -> Instruction:
    if 'on' in inst:
        fn = turn_on
    elif 'off' in inst:
        fn = turn_off
    elif 'toggle' in inst:
        fn = toggle
    else:
        raise Exception("I don't understand that instruction")

    coords = re.findall(r"\b\d[\d,.]*\b", inst)
    x, y = coords
    x = tuple((int(c) for c in x.split(',')))
    y = tuple((int(c) for c in y.split(',')))

    return (fn, x, y) 


def run_instructions(grid: Grid, instructions: List[Instruction], part: bool) -> Grid:
    for fn, x, y in instructions:
        grid = fn(grid, x, y, part)
    return grid


def data(file, parser=str, sep='\n') -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    with open(file) as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))


if __name__ == '__main__':
    import sys 

    file = sys.argv[1]
    part = int(sys.argv[2])
    if part == 1:
        part = False
    elif part == 2:
        part = True
    else:
        raise Exception(f"Don't know that part: {part}")

    instructions = data(file, parse_instructions)
    grid = np.zeros((1000, 1000))
    grid = run_instructions(grid, instructions, part)
    print(np.sum(grid))
