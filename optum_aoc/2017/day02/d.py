"""A python script to get the checkSum - Advent of Code day3.
"""

import pandas as pd

def checkSum(filepath):

    matrix = pd.read_csv(filepath, sep='\t', header=None)

    # Counter for answer
    total = 0;

    for index, row in matrix.iterrows():

        # Set a max counter as lowest int value
        currentMax = 0;
        # Set a min counter as high int value
        curentMin = 999999999;

        for x in row:
            # Set x to max if greater than currentMax
            if x > currentMax:
                currentMax=x
            if x < curentMin:
                curentMin=x

        total += currentMax - curentMin

    print(total)


def checkSumDivisible(filepath):

    matrix = pd.read_csv(filepath, sep='\t', header=None)

    # Counter for answer
    total = 0;

    # Loop through each row
    for index, row in matrix.iterrows():

        # Loop through each element
        for x in row:

            # Loop through each element again
            for y in row:

                # Make sure not comparing same element by x!=y
                # Check divisible no remainder by x%y == 0
                if (x!=y) & (x%y == 0):
                    total += x/y
                    # print("row number: ",index," element 1: ", x, " element 2: ", y)

    print(int(total))

if __name__ == '__main__':

    # Specify file path on local
    checkSum("input.txt")
    checkSumDivisible("input.txt")