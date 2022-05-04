import sys

def load_input(filepath):
    """
    Load input into list of ints.
    """
    with open(filepath, 'r') as s:
        nums = [int(e) for l in s for e in l]
    return nums

def get_stepped_index_func(s):
    """
    Returns a function (!) f which takes a list l and an index i and returns
    l[i+s] where we have looped l around so that the first element comes after
    the last.
    
    I don't think this is the most pythonic approach, probably better just to
    have a 3 argument function or subclass list and override indexing, but
    this is a good approach to be aware of.
    """
    def stepped_index(l, i):
        return l[(i+s)%len(l)]
    return stepped_index

def sum_nums(nums, steps=1):
    """
    Sum all numbers in nums for which the element in nums `steps` steps ahead
    of the number equals the number, where the list loops from the end to the
    start.
    """
    step_index = get_stepped_index_func(steps)
    
    result = 0

    for i in range(len(nums)):
        if nums[i] == step_index(nums, i):
            result += nums[i]

    return result


def main(filepath):
    nums = load_input(filepath)
    
    print('Part 1: {}'.format(sum_nums(nums)))
    print('Part 2: {}'.format(sum_nums(nums, len(nums)//2)))


if __name__=='__main__':
    filepath = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]
    main(filepath)