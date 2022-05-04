import sys


def parse_input(path):
    with open(path) as f:
        lines = [int(x) for x in f.readlines()]
    return lines


def part_1(depths):
    depth_comparison = depths[0]
    deeper = 0
    for i in depths:
        if i > depth_comparison:
            deeper += 1
        depth_comparison = i
    print('part 1', deeper)


def part_2(depths):
    depth_comparison = 0
    deeper = 0

    for i in range(1, len(depths) - 2):
        slider = sum(depths[i:i + 3])
        if slider > depth_comparison:
            deeper += 1
        depth_comparison = slider
    print('part 2', deeper)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python [script.py] [input.txt]')
    else:
        depths = parse_input(str(sys.argv[1]))
        part_1(depths)
        part_2(depths)
