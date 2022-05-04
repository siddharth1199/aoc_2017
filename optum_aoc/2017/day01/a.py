
def read_file(file):
    with open(file, 'r') as f:
        digits = [[int(c) for c in line.strip()] for line in f][0]
    return digits


def find_value_digits(file, lb):
    valid_digits = []
    for i in range(len(file)):
        if file[i] == file[i-lb]:
            valid_digits.append(file[i])
    return valid_digits


def main(file):
    digits = read_file(file)
    valid_digits = find_value_digits(digits, 1)
    print('Part 1:', sum(valid_digits))

    mid_way = int(len(digits)/2)
    valid_digits = find_value_digits(digits, mid_way)
    print('Part 2:', sum(valid_digits))


if __name__ == '__main__':
    main("../inputs/day_01.txt")