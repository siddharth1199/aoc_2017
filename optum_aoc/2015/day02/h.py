import os
import re
import numpy as np
import datetime

def main():
    with open("input.txt") as infile:
        total_paper = 0
        total_ribbon = 0
        start_time = datetime.datetime.now()
        for line in infile:
            m = re.search('([0-9]*)x([0-9]*)x([0-9]*)', line)
            if m:
                dims = [int(m.group(1)), int(m.group(2)), int(m.group(3))]
                # print(dims)
                surfaces = [dims[i] * dims[j] for i in range(3) for j in range(i + 1,3)]
                # print(surfaces)
                total_paper += (2 * sum(surfaces) + min(surfaces))

                bow_len = np.prod(dims)
                total_ribbon += ( (2 * (sum(dims) - max(dims))) + bow_len)

        processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
        print(total_paper)
        print(total_ribbon)
        print('process took {:.3f} msec'.format(processing_time))

if __name__ == "__main__":
    main()

