## While trying to optimise my brute force csolution came across this really nice one by Kevin Yap: https://github.com/iKevinY/advent/blob/master/2015/day20.py

import sys
CACHE = {}
def parse(input):
    with open(input, "r") as f:
        exp_pres = int(f.read())
    return exp_pres

def factors(n):
    if n in CACHE:
        return CACHE[n]
    CACHE[n] = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            CACHE[n] |= set([i, n//i])
    return CACHE[n]

def part_1(exp_pres):
    house = 0
    while sum(factors(house)) * 10 < exp_pres:
        house += 1
    return house

def part_2(exp_pres):
    house = 1
    while sum(x for x in factors(house) if (x * 50 >= house)) * 11 < exp_pres:
        house += 1
    return house

def main(input):
    exp_pres = parse(input)
    p1_house_num = part_1(exp_pres)
    p2_house_num = part_2(exp_pres)
    print(f'House number: {p1_house_num} receives at least {exp_pres} presents')
    print(f'House number: {p2_house_num} receives at least {exp_pres} presents')

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("USAGE: python [script.py] [input.txt]")
    if len(sys.argv) > 1:
        puzzle_input = sys.argv[1]
    else:
        puzzle_input = 'input.txt'
    main(puzzle_input)

