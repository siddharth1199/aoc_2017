# from datetime.datetime import time
import sys


def read_num(num):
    num_str = str(num)
    stack = []
    num_cnt = 1
    ans = ''
    for s in num_str:
        if not stack:
            stack.append(s)
            continue

        curr_num = stack[-1]

        if s == curr_num:
            num_cnt += 1
        else:
            ans = '{}{}{}'.format(ans, num_cnt, stack.pop())
            num_cnt = 1
            stack.append(s)

    if stack:
        ans = '{}{}{}'.format(ans, num_cnt, stack.pop())

    return ans


def main(num = 1113122113):
    # part 1
    num = open(sys.argv[1], 'r').read().strip()
    ans1 = num
    for i in range(50):

        ans1 = read_num(ans1)
        if i >= 39:
            print(i, len(ans1))
    print('Answer for part 1: ', len(ans1))

    # part 2
    # left = 1
    # right = 22113
    # for i in range(50):
    #     left = read_num(left)
    #     if i >= 40:
    #         print(i, len(left))
    #     # right = read_num(right)
    # print(len(left))


if __name__ == '__main__':
    main()
