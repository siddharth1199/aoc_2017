import sys
import re
sys.setrecursionlimit(10000)


def get_stats(file):
    with open(file, 'r') as f:
        input_dict = {}
        for i, line in enumerate(f):
            inst, r, _, sign, num = re.match(r'(...) ([a-b])?(, )?([+-])?([0-9]{1,3})?', line).groups()
            if sign == '-':
                num = int(num)*-1
            input_dict[i] = inst, r, num
    return input_dict


def apply_inst(input_dict, inst_ind, r):
    inst = input_dict[inst_ind][0]
    offset = input_dict[inst_ind][2]
    r_pos = 0 if input_dict[inst_ind][1] == 'a' else 1

    if (inst == 'jio' and r[r_pos] == 1) | (inst == 'jie' and r[r_pos] % 2 == 0) | (inst == 'jmp'):
        inst_ind += int(offset)

    else:
        inst_ind += 1
        if inst == 'inc':
            r[r_pos] = r[r_pos] + 1

        elif inst == 'tpl':
            r[r_pos] = (r[r_pos]) * 3

        elif inst == 'hlf':
            r[r_pos] = int((r[r_pos]) / 2)

    return inst_ind


def keep_going(input_dict, inst_ind, r):
    if inst_ind not in list(input_dict.keys()):
        return r
    #print(f'After instruction: {input_dict[inst_ind]}')
    inst_ind = apply_inst(input_dict, inst_ind, r)
    #print(inst_ind, r, '\n')
    return keep_going(input_dict, inst_ind, r)


def main(file, part_num):
    input_dict = get_stats(file)
    print(input_dict)
    inst_ind = 0
    r = [int(part_num)-1, 0]
    print(f'Final values in register: {keep_going(input_dict, inst_ind, r)}')


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])