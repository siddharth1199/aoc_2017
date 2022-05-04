import re


# Unashamedly stolen and adapted from Peter Norvig's Pytudes 2020
def data(day: int, parser=str, sep='\n') -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    with open(f'input.txt') as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))

def is_nice(s: str) -> bool:
    """
    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    """
    vowels = re.search(r"[aeiou].*[aeiou].*[aeiou]", s)
    twice = re.search(r"(.)\1", s)
    bad_pairs = re.search(r"ab|cd|pq|xy", s)
    if vowels and twice and not bad_pairs:
        return True
    else:
        return False


if __name__ == "__main__":
    strings = data(5)
    print(sum(is_nice(s) for s in strings))
