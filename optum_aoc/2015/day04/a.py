import hashlib
#import sys


def find_md5(key, starts_with):
    num=0
    while True:
        string_input = key + str(num)
        answer = hashlib.md5(string_input.encode()).hexdigest()
        if not answer.startswith(starts_with):
            num += 1
        else:
            break
    return num


def main():
    key = 'iwrupvqb'
    starts_with_part1 = '00000'
    starts_with_part2 = '000000'
    print("Part1: {}".format(find_md5(key,starts_with_part1)))
    print("Part2: {}".format(find_md5(key,starts_with_part2)))

    '''
    To execute the code with arguments
    print("Part1: {}".format(find_md5(sys.argv[1], sys.argv[2])))
    print("Part1: {}".format(find_md5(sys.argv[1], sys.argv[2])))
    '''


if __name__ == "__main__":
    main()
