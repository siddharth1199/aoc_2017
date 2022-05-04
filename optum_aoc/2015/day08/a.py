import re
import sys


def load_data(fname):
    with open(fname, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            yield line


def solve(fname):
    char_count = mem_count = ext_count = 0

    for line in load_data(fname):
        mem_count += len(line)
        char_count += (len(re.sub(r'(\\\")|(\\\\)|(\\x[0-9a-z]{2})', "$", line)) - 2)
        ext_count += len(re.sub(r'(\\)|(")', r"$$", line)) + 2

    return ((mem_count - char_count), (ext_count - mem_count))


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 2

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    print(solve(input_file)[part_num - 1])
