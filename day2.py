import numpy as np
import pandas as pd

WS = pd.read_csv('day2.txt', delim_whitespace=True, header=None)
np_arr = np.array(WS)
print('Part 1 =', (np.max(np_arr, axis=1) - np.min(np_arr, axis=1)).sum())