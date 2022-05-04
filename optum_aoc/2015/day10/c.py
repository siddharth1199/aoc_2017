import time
import sys

tic = time.time()
from itertools import groupby

#str1 = "1113222113"
str1 = open(sys.argv[1], 'r').read().strip()
counter = 0

while counter < 50:
    groups = groupby(str1)
    result = [(sum(1 for _ in group), label) for label, group in groups]
    j = []
    for i in range(len(result)):
        j += result[i]

    list_string = map(str, j)
    str1 = ''.join(list(list_string))
    counter += 1

print(len(str1))
toc = time.time()
print("Part 1 time:" + str(1000 * (toc - tic)) + " ms")