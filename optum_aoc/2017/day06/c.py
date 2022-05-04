"""
An object oriented solution. I don't think this is the best, but it was
educational.
"""
# We're going to subclass list, but doing that directly is a bad idea.
# Instead we'll user UserList, which is built for exactly this.
from collections import UserList


class CycleList(UserList):
    """
    A list that supports cyclic indexing, so that if
    l = CycleList([0, 1, 2])
    then l[3] will wrap around even though 3 is out of bounds usually, giving
    l[0].

    Also include some other helper methods.
    """

    def __getitem__(self, i):
        # The dunder method for indexing. 'data' comes from UserList,
        # it's the list of data within self.
        return self.data[i % (len(self.data))]

    def __setitem__(self, i, item):
        # Used for updating. I tried to use __getitem__ here but couldn't.
        self.data[i % (len(self.data))] = item
        pass

    def __iter__(self):
        # For iterating over data. Used implicitly when converting to tuple.
        # Need to override as due to the change in __getitem__, would cycle
        # infinitely otherwise.
        for i in range(len(self.data)):
            yield self.data[i]

    def argmax(self):
        # Return (i, v), where v is the max value and i is the first index of
        # that value.
        return max(enumerate(self.data), key=lambda x: x[1])

    def redistribute(self):
        # Perform the redistribute operation from the AoC problem inplace (!).
        max_ind, max_val = self.argmax()
        self[max_ind] = 0
        # We've done a lot of OOP to make these two lines pretty, essentially.
        for i in range(max_ind + 1, max_ind + 1 + max_val):
            self[i] += 1
        pass


def parse_input(filepath):
    # Read input and save to CycleList.
    with open(filepath, 'r') as f:
        nums = [int(x) for x in next(f).split()]
    return CycleList(nums)


def first_repeat_redistribution(cycle_list):
    """
    Given a cycle_list, return a pair (a, b) where
    a is the number of redistributions required to get a value previously seen
    b is the number of cycles in the resulting infinite loop.
    """
    # Make a copy of input as we will be overwriting.
    work_list = cycle_list.copy()
    # Create a tuple of list contents. Will need later.
    values = tuple(work_list)
    # List of previously seen iterations.
    seen = list()

    # While we have not seen the current result yet...
    while values not in seen:
        # Add the current result to previously seen list.
        # If we use work_list instead of tuple(work_list), then as CycleList
        # is mutable, when we update work_list in the line after, the value in
        # seen changes too! We 'immutify' work_list with tuple to avoid this.
        seen.append(values)
        # Redistribute work_list in place...
        work_list.redistribute()
        # ... and create new immutable values.
        values = tuple(work_list)

    # Find the first instance where 'values' was seen in the list. We know
    # values was seen previously. From this we calculate the number of cycles
    # in a loop.
    repeated_ind = next(i for i, v in enumerate(seen) if v == values)

    # Et voila.
    return len(seen), len(seen) - repeated_ind


def main(filepath):
    l = parse_input(filepath)
    print(first_repeat_redistribution(l))


if __name__ == '__main__':
    main('input.txt')