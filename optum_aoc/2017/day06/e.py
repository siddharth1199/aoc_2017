import time
import numpy as np

def parse(file_loc):
    """
    read input to numpy array
    :param file_loc: file path to AOC day6.txt
    """
    with open(file_loc) as f:
        input = f.read().split('\t')

    int_list = [int(i) for i in input]

    return np.array(int_list)


def find_max_value(np_array):

    return np.max(np_array)

def find_max_index(np_array):

    return np.argmax(np_array)

def spread_the_love(np_array, max_index, max_value):
    """Shares the value of the largest to the rest in the numpy array
     Returns numpy array where value shared."""

    # Code was causing issues until I added this in.
    # Kept altering np_matrix despite only supplying [-1] value to func
    np_array = np_array.copy()

    # Gets number and positions of indices to change (indices values go beyond length of array)
    indices = range(max_index + 1, max_index +1 + max_value)

    # Replace max value with zero
    np.put(np_array, max_index, 0)

    for i in indices:
        # Take the value at index i, add 1, then put it back into same position
        # Uses wrap which allows indicies > len array loops back to start
        new_value = np_array.take(i, mode='wrap') + 1
        np.put(np_array, i, new_value, mode='wrap')

    return np_array


def main(file_loc):

    np_array = parse(file_loc)

    # In order for vstack to work below, original array needs to be 2d
    np_matrix = np.atleast_2d(np_array)

    # While there's no duplicate arrays
    while(len(np_matrix) == len(np.unique(np_matrix, axis = 0))):

        love_shared = spread_the_love(np_matrix[-1], find_max_index(np_matrix[-1]), find_max_value(np_matrix[-1]))

        np_matrix = np.vstack([np_matrix, love_shared])

    print(f'The answer to part 1 is: {np_matrix.shape[0] - 1}')

    # np.where gives boolean 2d array..
    # array([[ True, False],
    #        [False, False]
    # .all(axis=1) where row is all true i.e. matches final array
    indicies_of_dupls = np.where((np_matrix == np_matrix[-1]).all(axis=1))

    print(f'The answer to part 2 is: {indicies_of_dupls[0][1]-indicies_of_dupls[0][0]}')

    return None


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'day6.txt'

    main(file_loc)

    end_time = time.time()
    print(f'Time taken:{(end_time - start_time)*1000} miliseconds')