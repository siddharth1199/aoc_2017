import re

def read_data(file):
    with open(file) as raw_data:
        data = raw_data.read()
    return [x for x in data.strip().splitlines() if x]

def rule1(string):
    return re.compile(r'([aeiou].*){3,}').search(string)

def rule2(string):
    return re.compile(r'(.)\1').search(string)

def rule3(string):
    return not re.compile(r'(ab|cd|pq|xy)').search(string)

def rule4(string):
    return re.compile(r'(..).*\1').search(string)

def rule5(string):
    return re.compile(r'(.).\1').search(string)

def apply_rules_part1(data,part1):
    for string in data:
        if rule1(string) and rule2(string) and rule3(string):
            part1 +=1
    return part1

def apply_rules_part2(data,part2):
    for string in data:
        if rule4(string) and rule5(string):
            part2 +=1
    return part2

def main():
    data = read_data('input.txt')
    part1 = 0
    part2 = 0
    print("Number of nice strings in Part 1: {}".format(apply_rules_part1(data, part1)))
    print("Number of nice strings in Part 2: {}".format(apply_rules_part2(data, part2)))

if __name__ == "__main__":
    main()
