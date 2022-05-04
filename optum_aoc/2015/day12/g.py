import sys
import re

# To keep track of types of brackets
BRACKETS = {'}': ('{', True),
            ']': ('[', False)}


def get_tokens(fname):
    with open(fname, 'r') as f:
        line = f.readline().strip()

    # Capturing only essential tokens i.e. {, [, ], }, numbers and red
    return re.findall(r"\{|\[|\]|\}|-?[0-9]+|red", line)


# Balanced Brackets Problem can be formulated by a context-free grammar.
# Using a pushdown automaton (PDA) to evaluate values within brackets.
def solve(tokens, part_num):
    stack = []
    end_brackets = tuple(BRACKETS.keys())

    for token in tokens:
        if token in end_brackets:
            values = BRACKETS[token]
            sum_val = 0
            is_red = False
            while True:
                top_token = stack.pop()
                top_is_red = (top_token == 'red')
                is_red = is_red | top_is_red

                if top_token == values[0]:
                    # Excluding the number if it's part 2 and there is a red within {}
                    if not ((part_num - 1) & is_red & values[1]):
                        stack.append(sum_val)
                    break
                else:
                    sum_val += 0 if top_is_red else int(top_token)
        else:
            stack.append(token)
    return stack[0]


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 2

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    print(solve(get_tokens(input_file), part_num))

