# Part 1

import time
import numpy as np

tic = time.time()

race_time = 2503


# race can be any arbitrary time

def instruction_parser(file):
    f = open(file, "r")
    instructions = f.readlines()
    parsed_instructions = []
    for single_string in instructions:
        words = single_string.split()
        parsed_instructions.append([int(words[3]), int(words[6]), int(words[-2])])
    return parsed_instructions


# returns list like this with speed, go_time, and rest_time
# [[ 22, 8, 165],
# [ 8, 17, 114],
# [ 18, 6, 103],
# [ 25, 6, 145],
# [ 11, 12, 125],
# [ 21, 6, 121],
# [ 18, 3, 50],
# [ 20, 4, 75],
# [ 7, 20, 119]]

# calculate the distance each reindeer covers in whole rounds
# then calculate the partial rounds.  At the end of the race, some reindeer may _xx_% through their go_time

def calculate_max_distance(parsed_instructions):
    total_distance = []
    for number in parsed_instructions:
        distance_per_round = (number[0] * number[1])
        time_per_round = (number[1] + number[2])
        whole_rounds = (int(race_time / time_per_round))
        whole_round_distance = whole_rounds * distance_per_round
        extra_seconds = round((race_time / time_per_round - whole_rounds) * time_per_round)
        if extra_seconds > number[1]:
            partial_distance = distance_per_round
        else:
            partial_distance = extra_seconds * number[0]
        total_distance.append(partial_distance + whole_round_distance)
    return ((total_distance))


print(max(calculate_max_distance(instruction_parser('input.txt'))))
toc = time.time()
print("Part 1 time:" + str(1000 * (toc - tic)) + " ms")

# Part 2
tic = time.time()


# use the same instruction parser from part 1


# logic: for each second of the race, the if statement calculates how many seconds into their whole_round (go_time + rest_time) each reindeer is.
# if the time of the race is <= to the go_time, distance is added, otherwise, the reindeer is stationary

def calculate_cumulative_distance(parsed_instructions):
    reindeer_distance = []
    for j in parsed_instructions:
        distance = 0
        total_distance = []
        for i in range(1, race_time + 1):
            if round(((i / (j[1] + j[2])) - int(i / ((j[1] + j[2]) + .01))) * (j[1] + j[2])) <= j[1]:
                distance += j[0]
            reindeer_distance.append(distance)
    return reindeer_distance


def best_reindeer(reindeer_distance):
    distances_array = np.array(
        [reindeer_distance[i:i + race_time] for i in range(0, len(reindeer_distance), race_time)])
    max_array = np.array(np.amax(distances_array, axis=0)).reshape((1, race_time))
    max_distance = np.zeros(distances_array.shape)
    for i in range(0, race_time):
        for j in range(len(distances_array)):
            if distances_array[j][i] == max_array[0][i]:
                max_distance[j][i] = 1
    return (max(max_distance.sum(axis=1)))


print(best_reindeer(calculate_cumulative_distance(instruction_parser('input.txt'))))
toc = time.time()
print("Part 2 time:" + str(1000 * (toc - tic)) + " ms")
