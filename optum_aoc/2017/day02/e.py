def read_file(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        entries = [[int(val) for val in e.split('\t')] for e in lines]
    return entries


def line_diff(line):
    return max(line) - min(line)


def evenly_divides(line):
    line.sort(reverse=True)
    for i, i_val in enumerate(line[:-1]):
        for j_val in line[i+1:]:
            if i_val % j_val == 0:
                return i_val / j_val


def main(file):
    entries = read_file(file)
    print(sum(line_diff(line) for line in entries))
    print(sum(evenly_divides(line) for line in entries))


if __name__ == '__main__':
    main("input.txt")