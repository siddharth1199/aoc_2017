import time

def string_to_list(s):
    """
    :param s: String with words separated by spaces
    :return: List of Strings
    """
    return s.split()


def is_list_unique(l):
    """
    :param l: List of string words
    :return: returns Boolean whether list is unique

    This function creates a new list of all elements in old list if they are not alreafdy added.
    Hence createing a unique list. Then compare if they are the same for unique or not.
    """
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist == l


def is_list_unique_using_set(l):
    """
    :param l: List of string words
    :return: returns Boolean whether list is unique

    This function uses set to keep unique values of list then compares length
    of supplied list and set to see if they are the same.
    If same then unique list
    """


    return (len(set(l)) == len(l))

def rearrange_string_alphabetically(w):
    """
    Takes in an unordered string (word) and rearranges it alphabetically

    :param w: String word
    :return: String word Ordered alphabetically
    """

    # Sorted() returns character list ordered. join() combines these into one string (word)
    return ''.join(sorted(w))

def solves_part1_par2():
    """
    :return part1_counter: count of how many phrases unique words
    :return part2_counter: count of how many phrases unique words and letters/word

    Answer to part one and two of problem
    """

    # Read file
    file = open('../AOC2017/input.txt', 'r')
    Lines = file.readlines()

    # counters for answers
    part1_counter = 0
    part2_counter = 0
    for line in Lines:

        # ****** PART 1 ******
        part1_counter += is_list_unique_using_set(string_to_list(line))


        # ****** PART 2 ******
        # Phrase to String List
        string_list = string_to_list(line)

        # Order words alphabetically
        sortList = [rearrange_string_alphabetically(i) for i in string_list]

        # Boolean True will return a 1
        part2_counter += is_list_unique_using_set(sortList)

    return part1_counter, part2_counter


if __name__ == '__main__':

    start_time = time.time()

    part_one1, part_one2 = solves_part1_par2()

    print(f"Total unique phrases with unique words  {part_one1}")

    print(f"Total unique phrases with unique words and letters {part_one2}")

    print('The code took {:.2f} milliseconds to execute'.format(1000*time.time() - start_time))