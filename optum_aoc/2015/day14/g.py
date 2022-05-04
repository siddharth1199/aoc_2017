import re
import sys
import datetime

start_time = datetime.datetime.now()
from collections import namedtuple

Reindeer = namedtuple('Reindeer', ['speed', 'fl_time', 'r_time'])


def parse(line):
    reindeer, speed, fl_time, r_time = re.match(
        r'(.*) can fly ([0-9]*) km/s for ([0-9]*) seconds, but then must rest for ([0-9]*) seconds.', line).groups()
    return reindeer, int(speed), int(fl_time), int(r_time)


def get_distances(file):
    rein_d = {}
    dist_d = {}
    points_d = {}
    with open(file, 'r') as f:
        for line in f:
            reindeer, speed, fl_time, r_time = parse(line)
            rein_d[reindeer] = Reindeer(speed, fl_time, r_time)
            dist_d[reindeer] = 0
            points_d[reindeer] = 0
    return rein_d, dist_d, points_d


def create_reindeer_dicts(rein_d, dist_dict, points_dict, start_time, end_time):
    for s in range(start_time, end_time):
        for r in rein_d.keys():
            _, remainder = divmod(s, (rein_d[r].fl_time + rein_d[r].r_time))
            if remainder < rein_d[r].fl_time:
                dist_dict[r] = dist_dict[r] + rein_d[r].speed
        highest = max(dist_dict.values())
        for r in rein_d.keys():
            if dist_dict[r] == highest:
                points_dict[r] += 1
    return max(dist_dict.items(), key=lambda k: k[1]), max(points_dict.items(), key=lambda k: k[1])


def main():
    dists, points = create_reindeer_dicts(*get_distances(sys.argv[1]), 0, 2503)
    print('{} travelled the furthest with a very respectable distance of {}m'.format(*dists))
    print('{} had the highest point total with {} points'.format(*points))

    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))


if __name__ == "__main__":
    main()
