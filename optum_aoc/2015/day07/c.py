import re
import sys

operations = {}
resolutions = {}

op_dict = {'ASGN': lambda x, y: y,
           'NOT': lambda x, y: ~y,
           'AND': lambda x, y: x & y,
           'OR': lambda x, y: x | y,
           'LSHIFT': lambda x, y: x << y,
           'RSHIFT': lambda x, y: x >> y}

def resolve(element):
    if element in resolutions:
        return resolutions[element]
    else:
        return run_operation(element)

def run_operation(operation):
    if operation.isnumeric():
        return int(operation)
    else:
        op = operations[operation]
        result = op[0](resolve(op[1]),resolve(op[2]))
        resolutions[operation] = result
        return result

def load_operations(fname):
    with open(fname,'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            
            # Two-operand operation: AND, OR, LSHIFT, RSHIFT
            m = re.search(r'(.*) (\w*) (.*) -> (\w*)', line)
            if m:
                elements = m.groups()
            else:
                # One-operand operation: NOT
                m = re.search(r'(\w*) (.*) -> (\w*)', line)
                if m:
                    elements = ('0', *m.groups())
                else:
                    # One-operand operation: Assignment
                    m = re.search(r'(.*) -> (\w*)', line)
                    if m:
                        elements = ('0', 'ASGN', *m.groups())
                    else:
                        elements = ()                        
                        
            if len(elements) > 0:
                operations[elements[3]] = (op_dict[elements[1]] , elements[0] , elements[2])


if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 2
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    load_operations(input_file)

    result = run_operation('a')
    if part_num == 2:
        resolutions = {}
        resolutions['b'] = result
        result = run_operation('a')
        
    print(result)