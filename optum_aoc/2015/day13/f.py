import sys
import re
from collections import defaultdict
import functools
import datetime

start_time = datetime.datetime.now()


## heavily inspired by Day 9 c.py!


class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight


def parse(line):
    name_1, sign, points, name_2 = re.match(r'(.*) would (.*) ([0-9]*) happiness units by sitting next to (.*).',
                                            line).groups()
    sign_points = -int(points) if sign == 'lose' else int(points)
    return name_1, sign_points, name_2


def held_karp(graph, include_me):
    """

    Rearrangement of Day 9 c.py function. Cycles through each name, starting from each name in turn,
    sums happiness in each direction for each seated pair for all names aside from starting name, eventual one name left in cycle,
    if include_me is True, no need to complete circle, i.e. happiness between first and last name doesn't need to be calculated
    if include_me if False, add happiness for first and last name in cycle.
    First name is defined by saving last name the first time it moves through the cycle
    f_name : first name
    l_name : last name
    o_name : other name, any name in subset (which shrinks throughout cycle) aside from last name

    lru_cache stores already worked out branches to prevent repeating work

    """

    @functools.lru_cache(maxsize=None)
    def happiness(subset, l_name, f_name=None):
        if f_name is None:
            f_name = l_name

        if len(subset) == 1:
            if include_me:
                return 0
            else:
                return graph.weights[(f_name, l_name)] + graph.weights[(l_name, f_name)]

        return max(happiness(subset - frozenset((l_name,)), o_name, f_name)
                   + graph.weights[(o_name, l_name)] + graph.weights[(l_name, o_name)]
                   # check happiness in both directions
                   for o_name in subset if o_name != l_name)

    return max(happiness(frozenset(graph.edges.keys()), name) for name in graph.edges.keys())


def main():
    graph = Graph()
    with open(sys.argv[1], 'r') as f:
        for line in f:
            n1, p, n2 = parse(line)
            graph.add_edge(n1, n2, p)

    print("Optimal happiness without me: {}".format(held_karp(graph, False)))
    print("Optimal happiness with me: {}".format(held_karp(graph, True)))
    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))


if __name__ == "__main__":
    main()
