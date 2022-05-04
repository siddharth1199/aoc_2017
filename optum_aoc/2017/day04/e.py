def parse_line(line):
    return line.rstrip().split()


def parse_input(filepath):
    with open(filepath, 'r') as f:
        out = [parse_line(line) for line in f]
    return out


def is_valid(words):
    if not words:
        return True
    else:
        head, tail = words[0], words[1:]
        if head in tail:
            return False
        else:
            return is_valid(tail)

def main():
    list_of_words = parse_input('input.txt')
    gen_of_sorted_words = (
        [sorted(w) for w in words] for words in list_of_words
    )
    num_valid_1 = sum(is_valid(words) for words in list_of_words)
    num_valid_2 = sum(is_valid(words) for words in gen_of_sorted_words)

    print(num_valid_1)
    print(num_valid_2)

if __name__=='__main__':
    main()