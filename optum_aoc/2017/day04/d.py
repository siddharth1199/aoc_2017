import time

def parse(file_loc):
    """
    read input to list
    :param file_loc: file path to AOC input.txt
    """
    input = open(file_loc, "r").read().split('\n')
    values=[]

    for line in input:
        values.append(line.split(' '))

    return values

def part_1(full_list):
    """
    part 1: using the set function, given a list of passcodes we check that the length of the passcode is the
    same length as the set of the passcode
    """
    count = 0
    for i in full_list:
        if len(i) == len(set(i)):
            count += 1

    return count

def part_2(full_list):
    """
    part 2: To check for anagrams, we sort the characters in each of the string items in a passcode and then uses the
    same method as part 1
    """
    count = 0
    for i in full_list:
        sorted_strings = []

        # sort the characters in a string
        for strings in i:
            sorted_strings.append(''.join(sorted(strings)))

        if len(sorted_strings) == len(set(sorted_strings)):
            count += 1

    return count


def main(file_loc):

    full_list = parse(file_loc)
    answer = part_1(full_list)
    answer2 = part_2(full_list)

    print(f'The answer to part 1 is: {answer}')
    print(f'The answer to part 1 is: {answer2}')

    return None


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'input.txt'

    main(file_loc)

    end_time = time.time()
    print(f'Time taken:{(end_time - start_time)*1000} miliseconds')