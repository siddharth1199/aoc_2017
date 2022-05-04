import re
from collections import defaultdict, namedtuple
import sys


def parse_input(input_path='input.txt'):
    Reindeer = namedtuple('Reindeer', ['speed', 'fly_duration', 'rest_duration'])
    reindeers = {}
    pattern = re.compile(r'(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    with open(input_path) as f:
        for line in f:
            reindeer, speed, fly_duration, rest_duration = re.match(pattern, line).groups()
            reindeers[reindeer] = Reindeer(int(speed), int(fly_duration), int(rest_duration))
    return reindeers


def solve_part1(competition_time, reindeers):
    answer1 = 0
    for _, fly_info in reindeers.items():
        speed, fly_duration, rest_duration = fly_info.speed, fly_info.fly_duration, fly_info.rest_duration
        n, remaining = divmod(competition_time, fly_duration + rest_duration)
        answer1 = max(answer1, speed * (n * fly_duration + min(remaining, fly_duration)))
    return answer1


def solve_part2(competition_time, reindeers):
    point_tracker = defaultdict(int)
    distance_so_far = defaultdict(int)
    time_flew_each_round = defaultdict(int)
    rest_until = defaultdict(int)

    farthest_distance = 0

    for t in range(1, competition_time + 1):
        # track the distance each reindeer has traveled at the end of second t
        for reindeer in reindeers.keys():
            if rest_until[reindeer] >= t:
                continue
            else:
                distance_so_far[reindeer] += reindeers[reindeer].speed
                rest_until[reindeer] += 1
                time_flew_each_round[reindeer] += 1

                farthest_distance = max(distance_so_far[reindeer], farthest_distance)

                if time_flew_each_round[reindeer] == reindeers[reindeer].fly_duration:
                    rest_until[reindeer] += reindeers[reindeer].rest_duration
                    time_flew_each_round[reindeer] = 0

        # Checking the tie
        for name, distance in distance_so_far.items():
            if distance == farthest_distance:
                point_tracker[name] += 1

    return max(point_tracker.values())


def main():
    if len(sys.argv) < 2:
        reindeers = parse_input()
    else:
        reindeers = parse_input(sys.argv[-1])

    competition_time = 2503

    answer1 = solve_part1(competition_time, reindeers)
    print('Answer for part 1: ', answer1)

    answer2 = solve_part2(competition_time, reindeers)
    print('Answer for part 2: ', answer2)


if __name__ == '__main__':
    main()
