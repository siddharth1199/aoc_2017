import time


def line_sep_file_to_list(l):

    list_offsets = list()

    [list_offsets.append(int(l.strip("\n"))) for l in Lines]

    return list_offsets


def leave_offset(list_offsets, i, question):

    if(question=="part1"):
        list_offsets[i] +=1
    else:
        # Part2
        if (list_offsets[i] >= 3):
            list_offsets[i] -= 1
        else:
            list_offsets[i] += 1

    return list_offsets


def calculate_number_jumps(list_offsets, question):


    jump_van_halen = True
    number_of_jumps = 0
    current_index = 0
    new_index = 0
    max_index = len(list_offsets) - 1  # 1056

    print(max_index)

    while jump_van_halen:

        # Determine where to jump
        # New index becomes the current index plus the value to jump by
        new_index += list_offsets[current_index]

        # Function to increment/decrease the offset pre jumping
        leave_offset(list_offsets, current_index, question)

        # Make the current index the new jumped one
        current_index = new_index

        # Increment counter of number of jumps
        number_of_jumps += 1

        # Checks to see if the new index post jumping would be out of bounds
        # If it is, the loop ends
        if (current_index > max_index):
            jump_van_halen = False

    return list_offsets, number_of_jumps



if __name__ == '__main__':

    start_time = time.time()


    # Read file
    file = open('day5.txt', 'r')
    Lines = file.readlines()

    # PART 1
    list_offsets, number_of_jumps = calculate_number_jumps(line_sep_file_to_list(Lines), "part1")

    print(f"Total number of jumps part 1  {number_of_jumps}")

    # Part 2

    list_offsets, number_of_jumps = calculate_number_jumps(line_sep_file_to_list(Lines), "part2")

    print(f"Total number of jumps part 2  {number_of_jumps}")

    print('The code took {:.2f} milliseconds to execute'.format(1000*time.time() - start_time))