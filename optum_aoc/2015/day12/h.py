import json
import time
import sys

def read_input(path):
    with open(path) as f:
        return json.load(f)

def has_red(data):
    for key, val in data.items():
        if key == 'red' or val == 'red':
            return True
    return False

def solve(data, part = 1):
    global SUM
    if isinstance(data, dict):
        if part == 2:
            if has_red(data):
                return
        for key, val in data.items():
            solve(key, part)
            solve(val, part)
    elif isinstance(data, list):
        for i in data:
             solve(i, part)
    elif isinstance(data, (int, float)):
        SUM += data
    return



def main(path = 'input.txt'):
    global SUM
    data = read_input(path)
    SUM = 0
    solve(data, part = 1)
    print('Answer for part 1: ', SUM)
    SUM = 0
    solve(data, part = 2)
    print('Answer for part 2: ', SUM)

if __name__ == '__main__':

    start = time.time()
    data_path = sys.argv[1]
    main(data_path)
    end = time.time()
    print('Time elapsed: ', end - start)
