import time
tic = time.time()

 

from functools import reduce

 

def factors(n):    
    return sum(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

 

def get_num_houses(total_gifts):
    houses = int((total_gifts**.5/(2**.5))/5) 
    while factors(houses) < (total_gifts/10):
        houses+=1
    return houses
n = 33100000
print(get_num_houses(n))
toc = time.time()
print("Part 1 time:" + str(1000*(toc-tic))+" ms")