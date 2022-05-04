import time
import sys
import pandas as pd
#import numpy as np


def checksum(df):
    """ for each row in df, computes checksum, the difference between greatest and smallest value
    then sums the checcksums for each row in the list of rows """
    diff = df.max(axis=1) - df.min(axis=1)
    return diff.sum()


def divisors(df):
    """ takes pandas df as input """
    list_of_lists = df.values.tolist()
    answer = 0
    for row_list in list_of_lists:
        answer_row = None
        for col_number, value in enumerate(row_list):
            if answer_row != None:
                break
            for index, other_value in enumerate(row_list):
                if col_number != index:  # we are comparing 2 different numbers in the row
                    if int(value) % int(other_value) == 0:
                        answer_row = int(value) / int(other_value)
                        break
        assert(answer_row != None), 'we didnt find a divisor on row {}'.format(row_list)
        answer += answer_row
    return answer


def main(file_loc):
    input_df = pd.read_csv(file_loc, sep='\t', header=None)
    answer_part_1 = checksum(input_df)
    answer_part_2 = divisors(input_df)
    return answer_part_1, answer_part_2


if __name__ == '__main__':
    start_time = time.time()
    input_file = 'input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

    answer_part_1, answer_part_2 = main(input_file)
    print('the solution to part a and b are {} and {}'.format(answer_part_1, answer_part_2))

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} milliseconds to execute'.format(1000*duration))