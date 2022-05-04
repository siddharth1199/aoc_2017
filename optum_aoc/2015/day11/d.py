''' As mentioned in below, regex is not practical for finding string of letters in alphabetical order:
    https://stackoverflow.com/questions/48588490/how-can-i-use-regex-to-find-a-string-of-characters-in-alphabetical-order-using-p
    So instead, implemented the conditions on numerical representations of passwords '''

import sys

FORBIDDEN_CHARS = (8, 11, 14)


def increment_password(digits):
    forbidden_char_index = [digits.index(i) for i in FORBIDDEN_CHARS if i in digits]

    # If hit 3rd condition, skip to next letter: e.g. hxbz(o)aaa -> hxbz(p)aaa
    if len(forbidden_char_index) > 0:
        new_digits = list(digits)
        max_idx = max(forbidden_char_index)
        new_digits[max_idx] = digits[max_idx] + 1
        for i in range(max_idx):
            new_digits[i] = 0
    # Otherwise generate next password: implementation of increment-by-one for base-26 '''
    else:
        new_digits = []
        carry = 1
        for digit in digits:
            new_digit = digit + carry
            if new_digit == 26:
                carry = 1
                new_digit = 0
            else:
                carry = 0
            new_digits.append(new_digit)

    # print(new_digits)
    return tuple(new_digits)


def solve(password):
    digits = tuple([(ord(c) - 97) for c in password][::-1])
    while True:
        digits = increment_password(digits)

        # Get indices of all instances of two consecutive identical characters. '''
        cons_inds = list(filter(lambda i: digits[i] == digits[i + 1], range(len(digits) - 1)))

        if all(tuple([any([((k == j - 1) & (k == i - 2)) for i, j, k in zip(digits, digits[1:], digits[2:])]),
                      not (any([i in FORBIDDEN_CHARS for i in digits])),
                      ((len(cons_inds) > 1) and (cons_inds[0] + 1 != cons_inds[-1]))])):
            return ''.join([chr(a + 97) for a in digits[::-1]])


if __name__ == "__main__":
    input_str = 'hxbxwxba'
    part_num = 2

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            input_str = f.readline().strip()
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    answers = []
    answers.append(solve(input_str))
    if part_num == 2:
        answers.append(solve(answers[0]))

    print(answers)
    #print(answers[part_num - 1])

