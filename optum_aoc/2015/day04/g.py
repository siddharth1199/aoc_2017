import hashlib 
import sys

def solve(puzzle_input,part_num):

    leading_len = 4 + part_num
    leading_str = '0'*leading_len
    
    i = 1
    # shameful brute force!
    while True:
        m = hashlib.md5()
        m.update(puzzle_input + str(i).encode('utf-8'))
        hash_string = m.hexdigest()
        
        if hash_string[:leading_len] == leading_str:
            return i
        else:
            i += 1
    
if __name__ == "__main__":
    # call this code with puzzle input and part number - default part number = 1
    part_num = 2
    if len(sys.argv) < 2:
        print('Please run with command-line arguments: python script.py puzzle_input [part_num]')
    else:
        if len(sys.argv) > 2:
            part_num = int(sys.argv[2])
    
        input_code = sys.argv[1].encode('utf-8')
        print(solve(input_code,part_num))
