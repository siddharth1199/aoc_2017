from operator import add


class Santa:
    def __init__(self):
        self.visited_homes = set()
        self.agent_location = [[0, 0]] * 2
        self.visited_homes.add(tuple(self.agent_location[0]))

    def move(self, agent, direction):
        self.agent_location[agent] = list(map(add, self.agent_location[agent], direction))
        self.visited_homes.add(tuple(self.agent_location[agent]))

    def solve(self, part_number=1):
        flip = part_number - 1

        directions = {'<': [-1, 0], '>': [1, 0], 'v': [0, -1], '^': [0, 1]}

        file = open('input.txt', 'r')

        char = file.read(1)
        agent = 0

        while char and (char not in ['\n', '']):
            self.move(agent, directions[char])
            agent = flip - agent
            char = file.read(1)

        file.close()

        print(len(self.visited_homes))


if __name__ == "__main__":
    part_number = 2  # Set to 1 or 2 to solve for respective part of the problem. Default: 1
    Santa().solve(part_number)
