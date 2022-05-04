import numpy as np
from typing import Callable


def read_input(file_path: str, delimiter: str = "\t"):
    """
    Read the spreadsheet file into a numpy ndarray.
    :param file_path: The file path
    :param delimiter: The delimiter used in the file. Defaults to "\t".
    :return: numpy 2D ndarray
    """
    spreadsheet = np.genfromtxt(fname=file_path, delimiter=delimiter)
    return spreadsheet


def get_rows_min_max(matrix: np.array) -> np.array:
    """
    Get an array of max-min difference from each row of the matrix.
    :param matrix: 2D spreadsheet of float numbers
    :return: Array of max-min differences for each row
    """
    return matrix.max(axis=1) - matrix.min(axis=1)


def get_rows_whole_division(matrix: np.array) -> np.array:
    """
    Get an array of whole division results from each row of the matrix.
    :param matrix: 2D spreadsheet of float numbers
    :return: Array of whole division results for each row
    """
    def row_whole_division(row: np.array) -> float:
        """
        Iterate over the row and find the result of a whole division between array elements if any.
        Note that only the first whole division result is returned and the search stops after that.
        :param row: A numpy 1D array
        :return: The whole division result for the given row
        """
        for ii, i in enumerate(row[:-1]):  # iterate over all elements of the array but the last one
            for j in row[ii + 1:]:  # iterate starting the next element in the row
                if i % j == 0:
                    return i / j
                elif j % i == 0:
                    return j / i
        # if no number pair was found to be evenly divisible, raise an exception
        raise Exception(f"the message is corrupt: no evenly divisible pairs found!")

    arr = np.apply_along_axis(func1d=row_whole_division, axis=1, arr=matrix)
    return arr


def get_checksum(ss: np.array, row_func: Callable[[np.array], np.array]) -> float:
    """
    Get the spreadsheet/matrix checksum with a given row logic function.
    :param ss: 2D spreadsheet of float numbers
    :param row_func: A function to apply on each row
    :return: Sum of all row results
    """
    checksum = sum(row_func(ss))
    return checksum


def main(file_path):
    spreadsheet = read_input(file_path=file_path)

    checksum_min_max = get_checksum(ss=spreadsheet, row_func=get_rows_min_max)
    print(f"the max-min checksum is {checksum_min_max:,.0f}")

    checksum_div = get_checksum(ss=spreadsheet, row_func=get_rows_whole_division)
    print(f"the whole division checksum is {checksum_div:,.0f}")


if __name__ == '__main__':
    main(file_path="input.txt")
