'''
The process consists of the following steps:
1. Let G_current be the boolean matrix representing current state of the light grid
2. Create matrix A to calculate 'ON' nieghbours of each light
3. Create boolean matrices B_on and B_off to check their corresponding conditions
4. Create C_on = B_on & G_current and C_off = B_off & invert(G_current) (flipped values)
5. G_next = C_on | C_off
'''


import sys
import numpy as np
import datetime
from scipy.ndimage.filters import generic_filter


def load_grid(fname):
    grid = np.zeros((100,100),dtype=np.bool)
    i = 0
    with open(fname,'r') as f:
        for line in f:
            line = line.strip()
            grid[i,:] = [True if c == '#' else False for c in line]
            i += 1
    return grid


def count_neighbours(arr):
    ''' The following filter slides through all lights to count neighbours:
          1 1 1
          1 0 1
          1 1 1
    '''
    foot_print = np.ones((3,3))
    foot_print[1,1] = 0

    ''' mode and cval define how to treat edges: here it adds a border of 0 to the grid '''
    return generic_filter(arr.astype(int), np.sum, footprint=foot_print, mode='constant', cval=0)


def check_conditions(neighbours, is_on=True):
    if is_on:
        return np.equal(neighbours, 3) | np.equal(neighbours, 2)
    else:
        return np.equal(neighbours, 3)

    
def flip_lights(grid, steps):
    def step(grid):
        x = count_neighbours(grid)        
        return (check_conditions(x,True) & grid) | (check_conditions(x,False) & np.invert(grid))
    
    if steps == 1:
        return step(grid)
    else:
        return flip_lights(step(grid), steps - 1)


if __name__ == "__main__":
    start_time = datetime.datetime.now()    
    input_file = 'input.txt'
    part_num = 2

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    grid = load_grid(input_file)
    grid = flip_lights(grid, 100)
        
    print(f'Part I answer: {grid.sum()}')
    processing_time = (datetime.datetime.now() - start_time).total_seconds()
    print(f'Calculations took {processing_time} seconds.')

