def parse_input(filepath):
    data = list()
    with open(filepath, 'r') as f:
        for l in f:
            data.append(int(l))
    
    return data

def take_step(offsets, instruction_index, steps):
    instruction = offsets[instruction_index]
    new_index = instruction_index + instruction

    if new_index in range(len(offsets)):
        offsets[instruction_index] += 1
        take_step(offsets, new_index, steps + 1)
    else:
        return steps + 1

    
def num_steps(offsets, increment_func = lambda x, y: 1):
    new_offsets = offsets.copy()

    instruction_index = 0
    steps = 0

    while instruction_index in range(len(new_offsets)):
        instruction = new_offsets[instruction_index]
        instruction_increment = increment_func(instruction, instruction_index)
        new_offsets[instruction_index] += instruction_increment
        instruction_index += instruction
        steps += 1
        
    return steps


def main(filepath):
    offsets = parse_input(filepath)
    print(num_steps(offsets))
    
    def part_2_update(instruction, instruction_index):
        return -1 if instruction >= 3 else 1

    print(num_steps(offsets, part_2_update))


if __name__=='__main__':
    main('input.txt')