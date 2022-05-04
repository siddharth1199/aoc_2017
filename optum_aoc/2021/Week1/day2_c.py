import time


def parse(file_loc):
    """
    read input to list
    :param file_loc: file path to AOC Day1_input.txt
    :return floor_depth: list of depths recorded on submarine
    """
    floor_depth = []
    with open(file_loc, "r") as myfile:
        for line in myfile:
            floor_depth.append(line)
    return floor_depth


def final_position(directions):
    """
    Checks the first letter of each line to see what direction is taken and takes the number, which is always position
    -2, to find the final position of the submarine
    :param directions: List of the directions in string form
    :return: horizontal and depth - both ints, the final horizontal and depth positions of the submarine
    """
    aim = 0
    depth = 0
    horizontal = 0
    for i in directions:
        if i[0] == 'f':
            horizontal = horizontal + int(i[-2])
            depth = depth + (aim * int(i[-2]))
        elif i[0] == 'u':
            aim = aim - int(i[-2])
        elif i[0] == 'd':
            aim = aim + int(i[-2])

    return horizontal, depth


def main(file):
    directions = parse(file)
    final_horiz, final_depth = final_position(directions)

    return final_horiz, final_depth


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'day2_input.txt'

    final_h, final_d = main(file_loc)
    print(f'The final horizontal position: {final_h}, The final depth is: {final_d}')
    print(f'Final position: {final_h * final_d}')

    end_time = time.time()
    print(f'Time taken:{end_time - start_time}')