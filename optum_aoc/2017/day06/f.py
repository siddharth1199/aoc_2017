import numpy as np


def read_file(filepath):
    # Read in the file
    with open(filepath) as f:
        input_list = f.read().split('\t')

    # Replace newline characters & make integers
    return [int(x.replace('\n', '')) for x in input_list]


def count_redistributions(input_list):
    """
    Perform the redistribution of blocks as in the question
    & return how many steps it takes before it repeats configurations

    Parameters
    ----------
    input_list: list
        A list of integers described in the question.

    Returns
    -------
    steps: int
        The number of steps taken to repeat a configuration.
    """

    # Set up an empty list to store all the configurations
    previous_lists = []

    # Append a copy of the input list to the previous_lists list
    previous_lists.append(input_list.copy())

    # Start the steps count
    steps = 0

    # Create a variable to check if all the configurations are unique
    unique_configs = True

    # Start the loop
    while unique_configs:

        # Step 1: identify the index with the max number of blocks (smallest index if theres a tie)
        max_index = np.argmax(input_list)

        # Step 2: find out how many blocks are in the bank at max_index
        max_value = input_list[max_index]

        # Step 3: set the current max_index value in the list to zero
        input_list[max_index] = 0

        # Step 4: create a list of the indices to add 1 to (as if the input list is infinitely long)
        indices_to_add_one_to = [max_index + (x + 1) for x in range(max_value)]

        # Step 5: correct the indices that are greater than the input list length with modular arithmetic
        indices_to_add_one_to_corrected = [x % len(input_list) for x in indices_to_add_one_to]

        # Loop over these indices and add 1 them in the input list
        for idx in indices_to_add_one_to_corrected:
            input_list[idx] += 1

        # Increment the number of steps taken
        steps += 1

        #  Check if the latest configuration is in the previous_lists list
        if input_list in previous_lists:

            print(f'Step {steps} produces a duplicated list...')

            # If it is then we've seen this configuration before so break the while loop
            unique_configs = False

            # For part 2 check which indexes are the duplicated ones
            existing_position = np.argmax([x == input_list for x in previous_lists])

            print(f"The list {input_list}\nappears at index {existing_position} & also at index {len(previous_lists)}")
            print(f"Size of loop: {len(previous_lists) - existing_position}")

        else:

            # Add a copy of the new cofiguration to the previous_lists list
            previous_lists.append(input_list.copy())

    return steps


if __name__ == '__main__':
    filepath = 'input.txt'

    # Read the file
    input_list = read_file(filepath)

    # Print out the answers
    count_redistributions(input_list)