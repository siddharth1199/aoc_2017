'''
README:

Unfortunately, this solution does not produce the right answer for part two.
I am not able to come up with a new solution due to the time constraints.

I tried bug shoot with the example in the problem description, and it worked perfectly.
One possible explanation I could think of is that the initial guess and the solver may affect the optimization.
With different initial guesses for part 1, I did get different answers.
But for part 2, I didn't have the luck to hit the right answer by varying the initial guess.
'''

from collections import namedtuple
import sys
import subprocess
import numpy as np


# Gekko is a python package that's capable of solving non-linear mixed integer optimization problems.
# For more information about gekko, check out https://gekko.readthedocs.io/en/latest/

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    from gekko import GEKKO

    print("module 'gekko' is installed")
except ModuleNotFoundError:
    print("module 'gekko' is not installed, installing the package")
    install("gekko")
    from gekko import GEKKO


def parse_input(input_path='input.txt'):
    ingredients = {}
    with open(input_path) as f:
        for line in f:
            words = line.split()
            ingredient, capacity, durability, flavor, texture, calories = words[0], words[2], words[4], words[6], words[
                8], words[10]
            ingredients[ingredient] = [int(capacity.strip(',')), int(durability.strip(',')), int(flavor.strip(',')),
                                       int(texture.strip(',')), int(calories.strip(','))]
    return ingredients


def solve_part1(data):
    # part 1

    # initialize gekko
    prob = GEKKO()
    prob.options.SOLVER = 1

    # initialize variables
    ingredients = list(data.keys())

    vars_dict = {}
    for i in ingredients:
        vars_dict[i] = prob.Var(value=0, lb=0, ub=100, integer=True)

    constraints_dict = {}
    properties = ['capacity', 'durability', 'flavor', 'texture', 'calories']
    property_idx = {prop: idx for idx, prop in enumerate(properties)}

    for prop in properties[:-1]:
        score = prob.sum([vars_dict[i] * data[i][property_idx[prop]] for i in ingredients])
        constraints_dict[prop] = score

        # decide to keep this constraint
        # I tried if2/if3 in Gekko to change the score to 0 when it goes negative, but it didn't work very well

        # keep the constraints and hope for a valid input that gives us a solution...
        prob.Equation(score >= 0)

    prob.Equation(prob.sum([i for i in vars_dict.values()]) == 100)

    # part 2
    # add the calories constraint
    prob.Equation(prob.sum([vars_dict[i] * data[i][property_idx['calories']] for i in ingredients]) == 500)

    # specify objective function, add a minus to convert a maximization problem to a minimization problem.
    prob.Obj(-np.prod([i for i in list(constraints_dict.values())]))
    prob.solve(disp=False)

    print('Results: ')
    for i in ingredients:
        print(i + str(vars_dict[i].value))

    print('Objective: ' + str(-prob.options.objfcnval))


def main():
    if len(sys.argv) < 2:
        data = parse_input()
    else:
        data = parse_input(sys.argv[-1])

    solve_part1(data)


if __name__ == '__main__':
    main()
