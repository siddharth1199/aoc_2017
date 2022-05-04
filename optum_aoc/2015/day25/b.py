import re

FIRST_CODE = 20151125


def read_loc(file):
    pattern = r"To continue, please consult the code grid in the manual.  Enter the code at row (\d*), column (\d*)."
    with open(file, 'r') as f:
        row, column = re.match(pattern, f.read()).groups()
        return int(row), int(column)


def next_code(prev):
    return (prev * 252533) % 33554393


def what_number(n):
    return n*(n+1)/2


def main(file):
    row, column = read_loc(file)
    pos_value = FIRST_CODE
    target_pos = what_number(row + column - 2) + column
    current_pos = 2

    while current_pos <= target_pos:
        pos_value = next_code(pos_value)
        #if current_pos%1000000 == 0:
            #print(f'Value at number {current_pos}: {pos_value}')
        current_pos += 1

    print(f'Based on position:\n - row: {row}\n - column: {column}\n'
          f'(position number {current_pos-1})\n\n--> Code to enter: {pos_value}')



if __name__ == "__main__":
    main("input.txt")