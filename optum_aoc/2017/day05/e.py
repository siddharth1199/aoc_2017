# Set the path to the input file
input_filepath = "/Users/jobrie30/Documents/Advent of Code/2017/Submissions/2017_day_5.txt"

# Open the input file
with open(input_filepath) as f:
    initial_input_list = f.read().split('\n')

# Make all the elements integers, not strings
input_list = [int(x) for x in initial_input_list]


# Make the function
def count_steps(input_list, part):
    
    """
    Play the game until you leave the list 
    and print out how many steps it took at the end
    
    Parameters
    ----------
    input_list: list
        A list of integers
        
    part: int
        Either 1 or 2
        
    Returns
    -------
    The number of steps taken to get out of input_list
    """
    
    # Set up initial values
    index = 0
    steps = 0
    
    # Create a copy of the input list, so we dont permanently change the list object outside the function
    input_list_copy = input_list.copy()

    # Use a while loop to check if we are within the list
    while index < len(input_list_copy):

        # Get the jump size by finding the value in current position in the input list
        jump_size = int(input_list_copy[index])
        
        # Check which part were doing
        if part == 1:
            
            # Update the input list by increasing the value in the current position by 1
            input_list_copy[index] += 1
        
        elif part == 2:
            
            # Check the jump size
            if jump_size >= 3:
                
                # Update the input list by decreasing the value in the current position by 1
                input_list_copy[index] -= 1
            
            else:

                # Update the input list by increasing the value in the current position by 1
                input_list_copy[index] += 1
            

        # Increase the index value with the jump size to get the next index
        index += jump_size

        # Increase the number of steps taken
        steps += 1

    print(f"It took {steps:,} steps to get out of the list for part {part} :)")


if __name__ == '__main__':

    # Part 1
    count_steps(input_list, 1)

    # Part 2
    count_steps(input_list, 2)
