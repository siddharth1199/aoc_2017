def read_input(file_name):
    with open(file_name) as file:
        lines = [i.strip('\n') for i in list(file)]
    return lines

def valid_passphrases(lines):
    return len([i for i in lines if sorted(list(set(i.split(' ')))) == sorted(i.split(' '))])

def valid_passphrases_secure(lines):
    return len([i for i in lines if sorted(set(list(map(''.join, list(map(sorted, i.split(' '))))))) == sorted(list(map(''.join, list(map(sorted, i.split(''))))))])

if __name__ == '__main__':
    lines = read_input('2017_day_4.txt')
    print('valid passphrases are {}'.format(valid_passphrases(lines)))
    print('valid passphrases under new system are {}'.format(valid_passphrases_secure(lines)))