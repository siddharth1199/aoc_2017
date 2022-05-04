import sys

def read_input(fname):
    with open('input.txt','r') as f:
        return f.readline().strip()
        
def calculate_sum_of_digits(input_str, part_num):
    sum_val = 0
    input_len = len(input_str)
    
    for i in range(input_len):
        digit = input_str[i]
        if part_num == 1:
            next_digit = input_str[(i + 1) % input_len]
        elif part_num == 2:
            next_digit = input_str[int((i + input_len / 2)) % input_len]
            
        if digit == next_digit:
            sum_val = sum_val + int(digit)
    return sum_val

if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 1

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    input_str = read_input(input_file)
    print(calculate_sum_of_digits(input_str, 1))