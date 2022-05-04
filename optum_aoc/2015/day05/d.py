import re
import sys

conditions = [[r'(.*[aeiou]){3}',
               r'.*(\w)\1',
               r'(?!.*(ab|cd|pq|xy))'],
              [r'.*(\w{2}).*\1',
               r'.*(\w).\1']]

nice_strings = []


def solve(fname, part_num):
    nice_strings = []
    with open(fname, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            if all([True if re.match(cond, line) else False for cond in conditions[part_num]]):
                nice_strings.append(line)
    return len(nice_strings)


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 2

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    print(solve(input_file, part_num - 1))
