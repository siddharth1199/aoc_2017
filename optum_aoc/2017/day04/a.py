import time
import sys


def generator_parse(file_loc):
    """ yields the input one line at a time, minimises storage requirement if file is massive """
    with open(file_loc, "r") as myfile:
        for line in myfile:
            input = line.strip()
            list_words = input.split()
            yield list_words


def check_duplicates(list_words):
    """ checks if list contains duplicates, returns boolean """
    set_words = set(list_words)
    if len(set_words) == len(list_words):
       return True
    else:
        return False


def check_anagrams(list_words):
    """ check if list of words contain any two words that are anagrams
    we just do sort of all words before comparison
    note this still catches duplicates, as duplicates are anagrams """
    sorted_list_words = []
    for word in list_words:
        sorted_list_words.append(''.join(sorted(word)))
    set_sorted_words = set(sorted_list_words)
    if len(set_sorted_words) == len(list_words):
        return True
    else:
        return False


def main(input_file):
    """ checks each input line to see if it is a valid password """
    total_valid_counts_part1 = 0
    total_valid_counts_part2 = 0
    for x in generator_parse(input_file):
        # part 1
        validity_boolean_part1 = check_duplicates(x)
        total_valid_counts_part1 += validity_boolean_part1
        # part 2
        validity_boolean_part2 = check_anagrams(x)
        total_valid_counts_part2 += validity_boolean_part2
    return total_valid_counts_part1, total_valid_counts_part2


if __name__ == '__main__':
    start_time = time.time()
    input_file = 'day04_input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

    answer_part_1, answer_part_2 = main(input_file)
    print('the solution to part a and b are {} and {}'.format(answer_part_1, answer_part_2))

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} milliseconds to execute'.format(1000*duration))