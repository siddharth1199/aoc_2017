import time
import re

tic = time.time()


# ord() converts characters to a number which makes it easy to increment by 1.

# I use ord() to find the straight of at least 3 characters

def straight_word(word):
    counter = 0
    for x in range(0, len(word) - 2):
        if (ord(word[x + 2]) - ord(word[x + 1])) == 1 and (ord(word[x + 1]) - ord(word[x])) == 1:
            counter = 1
    return counter


# regex to look for repeating letters.
# set() to count the unique pairs

def double_pair(word):
    counter = 0
    pattern = re.compile(r'(.)\1')
    iterator = re.findall(pattern, word)
    if len(set(iterator)) > 1:
        counter = 1
    return counter


def banned_letters(word):
    return not (bool(re.compile(r'(i|o|l)').search(word)))


# a little brute force here.  looking for words where the last letter is 'z' to manually increment.
# the good news is that these edge cases are pretty rare

def increment_word(input_word):
    i = ord(input_word[len(input_word) - 1])
    j = ord(input_word[len(input_word) - 2])
    k = ord(input_word[len(input_word) - 3])
    l = ord(input_word[len(input_word) - 4])
    m = ord(input_word[len(input_word) - 5])
    n = ord(input_word[len(input_word) - 6])
    o = ord(input_word[len(input_word) - 7])
    if i != 122:
        i += 1
        input_word = input_word[0:len(input_word) - 1] + chr(i)
    elif i == 122 and j == 122 and k == 122 and l == 122 and m == 122 and n == 122 and o == 122:
        i = ord(input_word[len(input_word) - 8:len(input_word) - 7])
        i += 1
        input_word = input_word[0:len(input_word) - 8] + chr(i) + 'aaaaaaa'
    elif i == 122 and j == 122 and k == 122 and l == 122 and m == 122 and n == 122:
        i = ord(input_word[len(input_word) - 7:len(input_word) - 6])
        i += 1
        input_word = input_word[0:len(input_word) - 7] + chr(i) + 'aaaaaa'
    elif i == 122 and j == 122 and k == 122 and l == 122 and m == 122:
        i = ord(input_word[len(input_word) - 6:len(input_word) - 5])
        i += 1
        input_word = input_word[0:len(input_word) - 6] + chr(i) + 'aaaaa'
    elif i == 122 and j == 122 and k == 122 and l == 122:
        i = ord(input_word[len(input_word) - 5:len(input_word) - 4])
        i += 1
        input_word = input_word[0:len(input_word) - 5] + chr(i) + 'aaaa'
    elif i == 122 and j == 122 and k == 122:
        i = ord(input_word[len(input_word) - 4:len(input_word) - 3])
        i += 1
        input_word = input_word[0:len(input_word) - 4] + chr(i) + 'aaa'
    elif i == 122 and j == 122:
        i = ord(input_word[len(input_word) - 3:len(input_word) - 2])
        i += 1
        input_word = input_word[0:len(input_word) - 3] + chr(i) + 'aa'
    else:
        i = ord(input_word[len(input_word) - 2:len(input_word) - 1])
        i += 1
        input_word = input_word[0:len(input_word) - 2] + chr(i) + 'a'
    return input_word


def find_perfect_word(word):
    word = increment_word(word)
    counter = 0
    while double_pair(word) + straight_word(word) + banned_letters(word) < 3:
        word = increment_word(word)
        counter += 1
    print("word: " + word + "; iterations: " + str(counter))
    return word  # Added by Andrew


#find_perfect_word('vzbxkghb')
word = find_perfect_word(open('input.txt').read().strip())
find_perfect_word(word)
toc = time.time()
print("Part 1 time:" + str(1000 * (toc - tic)) + " ms")