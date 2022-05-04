
# part 1
def readInput(file):
    with open(file, 'r') as f:
        lst = f.readlines()
    return [i.strip() for i in lst]

def getNbrCode(input_lst):
    res = 0
    for lst in input_lst:
        res += len(lst)
    return res

def getNbrMemory(input_lst):
    res = 0
    # escape sequence: \\, \", \x00
    for s in input_lst:
        temp_len = 0
        s = s[1:-1]
        n = len(s)
        p, p_check = 0, 0
        while p < n:
            curr_char = s[p]
            if curr_char == '\\':
                p_check = p + 1
                if s[p_check] == '"' or s[p_check] == '\\':
                    p = p_check + 1
                else:
                    p = p_check + 3
            else:
                p += 1

            temp_len += 1
        res += temp_len
    return res


# part 2

def getNbrNewEncode(input_lst):
    res = 0
    for s in input_lst:
        temp_len = 0
        p = 0
        n = len(s)
        while p < n:
            curr_char = s[p]
            # check special character: ", \
            if curr_char == '\"' or curr_char == '\\':
                temp_len += 1
            temp_len += 1
            p += 1
        # always plus 2
        temp_len += 2
        res += temp_len
    return res

def main(file):
    input_lst = readInput(file)
    nbrCode = getNbrCode(input_lst)
    nbrMemory = getNbrMemory(input_lst)
    nbrNewEncode = getNbrNewEncode(input_lst)
    print('Answer for part 1: ', nbrCode - nbrMemory)
    print('Answer for part 2: ', nbrNewEncode - nbrCode)

if __name__ == '__main__':
    file = 'input.txt'
    main(file)
