import sys
import datetime

start_time = datetime.datetime.now()

TOTAL_CAP = 150


def read_list(file):
    containers = []
    with open(file, 'r') as f:
        for line in f:
            containers.append(int(line.strip()))
        return containers


def container_combinations(numbers, cap, get_min_cont, min_cont, partial_sum=0, num_cont=0):
    if num_cont > min_cont:
        return
    if partial_sum == cap:
        if get_min_cont:
            min_cont = num_cont
            yield num_cont
        else:
            yield 1
    if partial_sum >= cap:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from container_combinations(remaining, cap, get_min_cont, min_cont, partial_sum+n, num_cont+1)


def main(puzzle_input):
    containers = read_list(puzzle_input)
    containers.sort(reverse=True)
    print(f'All combinations of containers that add up to {TOTAL_CAP}: {sum(container_combinations(containers, TOTAL_CAP, False, len(containers), partial_sum=0, num_cont=0))}')

    min_cont = min(container_combinations(containers, TOTAL_CAP, True, len(containers), partial_sum=0, num_cont=0))
    print(f'All combinations of {min_cont} containers that add up to {TOTAL_CAP}: {sum(container_combinations(containers, TOTAL_CAP, False, min_cont, partial_sum=0, num_cont=0))}')

    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} milliseconds".format(processing_time))


if __name__ == "__main__":
    main(sys.argv[1])
