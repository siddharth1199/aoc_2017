import time
import sys


class SpiralClass:
    """ Class that builds a spiral grid one move at a time """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xmin = 0
        self.xmax = 0
        self.ymin = 0
        self.ymax = 0
        self.direction = 'right'
        self.index_to_xy_mapping = {1: (0, 0)}
        self.xy_to_index_mapping = {(0, 0): 1}
        self.counter = 1
        self.value_mapping = {1: 1}

    def one_move(self):
        """ adds one extra element to the spiral """
        assert (self.direction in ['left', 'right', 'up', 'down'])
        self.counter += 1

        new_direction = None
        if self.direction == 'right':
            if self.x > self.xmax:
                new_direction = 'up'
                self.xmax = self.x
                self.y += 1
            else:
                self.x += 1
        elif self.direction == 'up':
            if self.y > self.ymax:
                new_direction = 'left'
                self.ymax = self.y
                self.x += -1
            else:
                self.y += 1
        elif self.direction == 'left':
            if self.x < self.xmin:
                new_direction = 'down'
                self.xmin = self.x
                self.y += -1
            else:
                self.x += -1
        elif self.direction == 'down':
            if self.y < self.ymin:
                new_direction = 'right'
                self.ymin = self.y
                self.x += 1
            else:
                self.y += -1

        if new_direction != None:
            self.direction = new_direction

        self.index_to_xy_mapping[self.counter] = (self.x, self.y)
        self.xy_to_index_mapping[(self.x, self.y)] = self.counter

        def value_computer(x, y):
            """ computes value of position by summing all adjacent squares values """
            value = 0
            for x_offset in [-1, 0, 1]:
                for y_offset in [-1, 0, 1]:
                    if x_offset == 0 and y_offset == 0:
                        continue
                    elif (x + x_offset, y + y_offset) in self.xy_to_index_mapping:
                        neighbour_index = self.xy_to_index_mapping[(x + x_offset, y + y_offset)]
                        value += self.value_mapping[neighbour_index]
            return value

        self.value_mapping[self.counter] = value_computer(self.x, self.y)

        return None


def spiral_cord(index):
    """ returns the x, y cordinates of an index following spiral """
    first_larger_value = None
    spiral_instance = SpiralClass()
    while spiral_instance.counter < index:
        spiral_instance.one_move()
        if first_larger_value == None:  # stops overwriting the new first larger value every time
            if spiral_instance.value_mapping[(spiral_instance.counter)] > index:
                first_larger_value = spiral_instance.value_mapping[(spiral_instance.counter)]

    return spiral_instance.x, spiral_instance.y, first_larger_value

def main(input_value):
    x_pos, y_pos, big_value = spiral_cord(input_value)
    answer_part_1 = abs(x_pos)+abs(y_pos)
    return answer_part_1, big_value


if __name__ == '__main__':
    start_time = time.time()
    input_value = 312051

    if len(sys.argv) >= 2:
        input_value = sys.argv[1]

    answer_part_1, answer_part_2 = main(input_value)
    print('the solution to part a and b are {} and {}'.format(answer_part_1, answer_part_2))

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} milliseconds to execute'.format(1000*duration))