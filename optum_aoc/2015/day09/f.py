import re
import sys
import os
import numpy as np
import itertools

MAX_NODES = 10

rows = cols = MAX_NODES
adj_mat = np.full(shape=(MAX_NODES,MAX_NODES),fill_value=-1,dtype=np.int16)

node_dict = {}

OPERATIONS = (lambda x,y: min(x,y),
              lambda x,y: max(x,y))


def create_graph(fname):
    next_index = 0
    with open(fname,'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            elements = re.search(r'(\w*) to (\w*) = ([0-9]*)', line).groups()
            
            for i in range(2):
                if elements[i] not in node_dict:
                    node_dict[elements[i]] = next_index
                    adj_mat[next_index][next_index] = 0
                    next_index += 1
                    
            nodes = (node_dict[elements[0]], node_dict[elements[1]])
            adj_mat[nodes[0],nodes[1]] = int(elements[2])
            adj_mat[nodes[1],nodes[0]] = int(elements[2])
        

def solve_brute_force(part_num):
    node_count = len(node_dict)    
    perms = itertools.permutations(range(node_count))
    opt_dist = (3 - 2 * part_num) * np.Inf
    for perm in perms:
        curr_dist = 0
        for i in range(len(perm) - 1):
            curr_dist += adj_mat[perm[i],perm[i+1]]
        opt_dist = OPERATIONS[part_num - 1](opt_dist,curr_dist)
        
    return opt_dist

            
if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 1

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    create_graph(input_file)
    print(solve_brute_force(part_num))
