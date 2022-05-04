from collections import defaultdict


def read_data(file):
    with open("input.txt") as raw_data:
        data = raw_data.read()
    return [x for x in data.strip().splitlines() if x]


def update_houses(houses, pos):
    if pos in houses.keys():
        houses[pos] += 1
    else:
        houses[pos] = 1
    return pos, houses


def distinct_houses(houses, total_houses):
    for key in houses.keys():
        total_houses += 1
    return total_houses


def houses_with_prize(data, pos, houses):
    for c in data[0]:
        (x, y) = pos
        if c == '^':
            pos = (x, y + 1)
        elif c == 'v':
            pos = (x, y - 1)
        elif c == '<':
            pos = (x - 1, y)
        elif c == '>':
            pos = (x + 1, y)
        pos, houses = update_houses(houses, pos)
    return pos, houses


def robo_santa(data, houses):
    pos_santa = (0, 0)
    pos_robo = (0, 0)
    santa = True
    robo = False
    for c in data[0]:
        if santa:
            pos_santa, houses  = houses_with_prize(c, pos_santa, houses)
            santa = False
            robo  = True
        elif robo:
            pos_robo, houses   = houses_with_prize(c, pos_robo, houses)
            robo  = False
            santa = True
    return houses


def main():
    houses = defaultdict(int, {(0,0):2})
    data = read_data("input.txt")
    houses = robo_santa(data, houses)
    print("Houses receiving at least one present: {}".format(distinct_houses(houses, 0)))


if __name__ == "__main__":
    main()
