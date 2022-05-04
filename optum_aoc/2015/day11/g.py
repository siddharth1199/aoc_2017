import string
import regex as re
import re
import sys
import time

req1 = {'abc', 'bcd', 'cde', 'def', 'efg', 'fgh',
        'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz'}

req1_pattern = '|'.join(req1)
req2_exclude = {'i', 'o', 'l'}

valid_letter = [i for i in string.ascii_lowercase if i not in req2_exclude]
alpha_to_num = {letter: idx for idx, letter in enumerate(valid_letter)}

# adding i, l, o in case the input has the three letters
alpha_to_num['i'] = 7
alpha_to_num['l'] = 9
alpha_to_num['o'] = 11

num_to_alpha = {idx: letter for idx, letter in enumerate(valid_letter)}


def check_req1(s):
    return re.finditer(req1_pattern, s)


def check_req3(s):
    pattern = r'([a-z])\1'
    return len(set(re.findall(pattern, s)))


def check_pass(s):
    # check requirement 1
    iterator = check_req1(s)
    for _ in iterator:
        # requirement 2 is met when generating the new password
        # check requirement 3
        if check_req3(s) >= 2:
            return True
    return False


def get_next(password_lst, idx):
    '''
    password is a list of letters in the password
    '''
    if idx == -1:
        print('The password has reached its upper bound')
        return
    else:

        curr = alpha_to_num[password_lst[idx]]
        if curr == 22:
            password_lst[idx] = 'a'
            get_next(password_lst, idx - 1)
        else:
            password_lst[idx] = num_to_alpha[curr + 1]
            return


def main(password):
    p = False
    pass_lst = list(password)
    while not p:
        get_next(pass_lst, 7)
        password = ''.join(pass_lst)
        p = check_pass(password)

    return ''.join(pass_lst)


if __name__ == '__main__':
    # password = 'vzbxxyzz'

    start = time.time()
    password = open(sys.argv[1], 'r').read().strip()

    for idx, w in enumerate(password):
        if w in req2_exclude:
            password = password[:idx] + num_to_alpha[alpha_to_num[w] + 1] + 'a' * (7 - idx)
            break

    print('input is ', password)
    ans1 = main(password)
    ans1_str = ''.join(ans1)
    print('Answer for part1: ', ans1_str)
    ans2 = main(ans1_str)
    ans2_str = ''.join(ans2)
    print('Answer for part2: ', ans2_str)
    end = time.time()

    print('time elapsed: ', end - start)
