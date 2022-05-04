from itertools import combinations
import time


def find_correct_containers(file):
    container_size = []
    f = open(file, 'r')
    for i in f:
        num = int(i.strip())
        container_size.append(num)
    """
leat_number_containers and most_number_containers wil help limit the overall number of combimations we try.
For example, if you sort the containers in descending order, you get:

    Container size:          Cumulative sum
    50                        50
    48                        98
    45                        143
    44                        187

You know that under any circumstance, you'll need at least 4 containers to reach 150.  

Likewise, if we sort in ascending order, you'll see we need at most 10 containers to reach 150.
    """
    least_number_containers = 0

    container_sum = 0
    container_size.sort(reverse=True)
    for num in container_size:
        if container_sum > 150:
            break
        container_sum += num
        least_number_containers += 1

    exact_matches = 0
    for i in range(least_number_containers, least_number_containers + 1):
        comb = combinations(container_size, i)
        for i in list(comb):
            if (sum(i)) == 150:
                exact_matches += 1
    return exact_matches


start_time = time.time()
print(find_correct_containers('input.txt'))
end_time = time.time()
duration = end_time - start_time
print('The code took {:.2f} milliseconds to execute'.format(1000 * duration))
