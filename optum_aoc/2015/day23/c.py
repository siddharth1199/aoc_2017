''' Day 23 Advent of Code, instructions '''

import sys
import time


def parse(file_loc):
    """
    creates nested list of instructions,
    each instruction contains nested list with [function, variable, amount]
    """
    instruction_list = []
    with open(file_loc, "r") as myfile:
        for line in myfile:
            things = line.replace(',', '').strip().split(' ')
            instruction_list.append(things)
    return instruction_list


def single_instruction_executor(instruction, current_number, reg_dict):
    """ note this to be a sub routine it acts on registers in main body """
    if instruction[0] == 'jmp':
        current_number += int(instruction[1])
        return current_number

    elif instruction[0] == 'inc':
        if instruction[1] == 'a':
            reg_dict['REG_A'] += 1
        else:
            reg_dict['REG_B'] += 1
        current_number += 1
        return current_number

    elif instruction[0] == 'hlf':
        if instruction[1] == 'a':
            reg_dict['REG_A'] //= 2  # rounding down, no floats allowed
        else:
            reg_dict['REG_B'] //= 2  # rounding down, no floats allowed
        current_number += 1
        return current_number

    elif instruction[0] == 'tpl':
        if instruction[1] == 'a':
            reg_dict['REG_A'] *= 3
        else:
            reg_dict['REG_B'] *= 3
        current_number += 1
        return current_number

    elif instruction[0] == 'jio':  # jump if one, not jump if odd!!!
        if instruction[1] == 'a':
            if reg_dict['REG_A'] == 1:
                current_number += int(instruction[2])
                return current_number
            else:
                current_number += 1
                return current_number
        else:
            if reg_dict['REG_B'] == 1:
                current_number += int(instruction[2])
                return current_number
            else:
                current_number += 1
                return current_number

    elif instruction[0] == 'jie':
        if instruction[1] == 'a':
            if reg_dict['REG_A'] % 2 == 0:
                current_number += int(instruction[2])
                return current_number
            else:
                current_number += 1
                return current_number
        else:
            if reg_dict['REG_B'] % 2 == 0:
                current_number += int(instruction[2])
                return current_number
            else:
                current_number += 1
                return current_number

    else:
        print('invalid instruction')
        return None


def multiple_instructions(reg_dict, instruction_list):
    """ conducts multiple instructions on list, this is sub routine, acts directly on registers in main body """
    total_number_instructions = len(instruction_list)
    instruction_number = 0

    while instruction_number < total_number_instructions:
        instruction_number = single_instruction_executor(instruction_list[instruction_number], instruction_number, reg_dict)

    return None


if __name__ == '__main__':
    start_time = time.time()
    input_file = 'input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

    instructions = parse(input_file)

    REGISTERS = {'REG_A': 0,
                 'REG_B': 0}

    multiple_instructions(REGISTERS, instructions)

    print(f'the value of the registers at the end of the instructions is {REGISTERS}')

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} seconds to execute'.format(duration))
