import sys
sys.setrecursionlimit(100000)

dat = open('input.txt', 'r').read()


def part1(dat):
    return dat.count('(') - dat.count(')')

p1 = part1(dat)

def part2(dat, idx, acc):
    if acc < 0:
        return idx
    elif dat[0] == '(':
        return part2(dat[1:], idx + 1, acc +1)
    elif dat[0] == ')':
        return part2(dat[1:], idx + 1, acc - 1)

p2 = part2(dat, 0, 0)

print('Part1: {}'.format(p1))
print('Part2: {}'.format(p2))
