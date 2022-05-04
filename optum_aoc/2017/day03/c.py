import time


def main(puzzle_input):
    """
    First we need to know how many spirals it takes to get to the outermost spiral where our puzzle input is.
    Eg. if it was 29 this would be the 3rd spiral.

         37 36 35 34 33 32 31
         38 17 16 15 14 13 30               round 1 - 8 (2-9)
         39 18 5  4  3  12 29
         40 19 6  1  2  11 28               round 2 - 8*2 (10 - 25)....
         41 20 7  8  9  10 27
         42 21 22 23 24 25 26
         43 44 45 46 47 48 49

        We only need to go in 2 directions to reach the centre. We know how many steps we need to go in one direction,
        3 in this example. We need to know how many steps are needed in the other direction. To do this we need to know
        what position (or side of the square) our puzzle input is on the outer most spiral. We can do this using the
        length of the outer most spiral (7 in this example). Last thing to do is check how many steps we need to take to
        the half way row (whether it's horizontal or vertical).In this case - 1. Total steps = 3+1 = 4.
    """

    # setting up loop with parameters of first spiral
    starting_point = 1
    end_point = 9
    i = 1
    while puzzle_input > end_point:  # continue through the spirals until the endpoint is > input
        i += 1  # keeping track of spirals
        starting_point = end_point  # update parameters
        end_point += 8 * i

    print(f'Puzzle input is on the {i}th spiral')

    # find the length of one side of outermost spiral
    square_len = 1 + i * 2
    print(f'Outermost spiral begins at: {starting_point}')

    outer_row_position = puzzle_input - starting_point
    print(f'Puzzle input is {outer_row_position} numbers around the outermost spiral')

    initial_pos = square_len - 1  # always start the next spiral on the second position from the bottom

    # we need to find the position of our puzzle input on one of the sides of the square
    j = outer_row_position - initial_pos
    if j >= square_len:  # iterate until the further corner is greater that our puzzle - we know it is in that 'side'
        while j >= square_len:
            j = j - (square_len - 1)

    steps_to_center = abs((i - j))
    print(f'Steps needed to get to the centre: {steps_to_center}')

    total_steps = i + steps_to_center

    return total_steps


if __name__ == '__main__':
    start_time = time.time()
    puzzle_input = 312051

    total_steps = main(puzzle_input)

    print(f'Steps needed to get to the centre: {total_steps}')
    end_time = time.time()
    print(f'Time taken:{end_time - start_time}')
