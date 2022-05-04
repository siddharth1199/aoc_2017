import numpy as np
import pandas as pd

grid = pd.read_csv('input.txt', delim_whitespace=True, header=None)
np_grid = np.array(grid)
print('Part 1 =', (np.max(np_grid, axis=1) - np.min(np_grid, axis=1)).sum())