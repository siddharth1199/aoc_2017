import sys


def parse_file(path):
    with open(path) as f:
        sequence = list(map(int, f.readline()))
    return sequence


def solve(seq, part):
    items = len(seq)
    if part == 1:
        step = 1
    elif part == 2:
        step = items // 2
    else:
        print('Wrong input')
        return
    return sum(n for i, n in enumerate(seq) if n == seq[i - step])


def main(path):
    seq = parse_file(path)
    print(f'part 1 = {solve(seq, 1)}')
    print(f'part 1 = {solve(seq, 2)}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python [script.py] [input.txt]')
    else:
        main(sys.argv[1])
