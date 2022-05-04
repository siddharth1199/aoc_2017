import sys

comb_lengths = []
amount_left = 150


def load_input(fname):
    data_rows = []
    with open(fname, 'r') as f:
        i = 0
        while True:
            line = f.readline().strip()
            if not line:
                break

            data_rows.append(tuple([i, int(line)]))
            i += 1
    data_rows = sorted(data_rows, key=(lambda x: x[1]), reverse=True)
    return data_rows


def find_combination(amount_left, containers_left, containers_used):
    combinations = 0
    for i, element in enumerate(containers_left):
        new_amount_left = amount_left - element[1]
        new_containers_used = [element] + containers_used.copy()
        if new_amount_left == 0:
            comb_lengths.append(len(new_containers_used))
            combinations += 1
        elif new_amount_left > 0:
            new_containers_left = containers_left[i + 1:].copy()
            combinations += find_combination(new_amount_left, new_containers_left, new_containers_used)
    return combinations


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 1

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    all_containers = load_input(input_file)

    val = find_combination(amount_left, all_containers, [])
    min_val = min(comb_lengths)

    print('{} {}'.format('Part I:', val))
    print('{} {}'.format('Part II:', len([x for x in comb_lengths if x == min_val])))