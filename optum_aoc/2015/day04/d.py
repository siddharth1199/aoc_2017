import sys
from hashlib import md5


def get_md5_hex(secret_key, value):
    if type(value) != int:
        raise TypeError(' {}: {} should be int'.format(value, type_value))
    elif value < 1:
        raise ValueError('value {} must be > 0'.format(value))
    proposed = (secret_key + str(value)).encode('utf-8')
    hexval = md5(proposed).hexdigest()
    return hexval


def find_value(secret_key, n_zeros, start=1):
    """
    Simple incremental loop that checks each integer in turn.
    Optional starting point, if you don't want to start at 1
    each time.

    :param secret_key: str - your puzzle input
    :param n_zeros: int - number leading zeros we want to find
    :param start: int - optional starting point. Skip checking [1, start -1]
    """

    if n_zeros < 0:
        raise ValueError('n_zeros should be non-negative')

    check = '0' * n_zeros
    i = start
    while True:
        hexval = get_md5_hex(secret_key, i)
        if hexval.startswith(check):
            return i
        i += 1


def main(secret_key):

    # examples
    # assert find_value('abcdef', 5) == 609043
    # assert find_value('pqrstuv', 5) == 1048970

    part1 = find_value(secret_key, 5)
    print('Part 1: {}'.format(part1))

    part2 = find_value(secret_key, 6, start=1)
    print('Part 2: {}'.format(part2))


if __name__ == '__main__':
    main(sys.argv[1])
