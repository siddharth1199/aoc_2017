"""
We make use of some mathematical bounds to skip on the smaller solutions.
We know that the sum of divisors is bounded above by some number, and so
we can skip all numbers for which we know the answer wil be less than what
we're looking for.

(Note that the number of presents at house n is related to the sum of divisors
of n.)

This solution assumes the Riemann hypothesis is true!

I think to speed this up further would require some parrelelism.
"""
from itertools import count

from math import ceil

import sympy as sp
from sympy import EulerGamma

TARGET = 33100000
MAX_HOUSES_PER_ELF = 50


def robins_upper_bound(n):
    """
    For all n > 5040, the sum of divisors of n is less than this
    https://en.wikipedia.org/wiki/Divisor_function
    """

    return sp.exp(EulerGamma) * n * sp.log(sp.log(n))


def robins_global_upper_bound(n):
    """
    Upper bound for the sum of divisors of n
    https://en.wikipedia.org/wiki/Divisor_function
    """
    return sp.Piecewise(
        (robins_upper_bound(n), n > 5040),
        (robins_upper_bound(n) + ((0.6483 * n)/(sp.log(sp.log(n)))), True)
    )


def get_lower_bound(target):
    """
    Given sum target, find the smallest possible n for which the
    sum of divisors could be as big as the target, according to
    robins upper bound
    """
    n = sp.Symbol('n')
    
    upper_bound = robins_global_upper_bound(n)
    guess = target*sp.exp(-EulerGamma).evalf()
    lower_bound = int(sp.nsolve(upper_bound - target, n, guess))
    
    return lower_bound


def get_sum_divisors(n, max_houses=MAX_HOUSES_PER_ELF):
    divisors = sp.divisors(n)
    non_lazy_divisors = (d for d in divisors if n//d <= max_houses)
    
    return sum(divisors), sum(non_lazy_divisors)


def get_first_houses(target, scale_factor_1=10, scale_factor_2=11,
                     verbose=True):
    """
    Given a target and starting value, find the first integer n greater than
    or equal to start such that the sum of divisors of n is at least as big as
    target
    """
    largest_scale_factor = max(scale_factor_1, scale_factor_2)

    start = get_lower_bound(target//largest_scale_factor)
    
    if verbose:
        print("Begining search from house {}".format(start))

    sol1_found = False
    sol2_found = False
    
    i = start
    while not (sol1_found and sol2_found):
        sum_divisors, sum_lazy_divisors = get_sum_divisors(i)
        if not sol1_found:
            presents1 = scale_factor_1*sum_divisors
            if presents1 >= target:
                sol1_found = True
                sol1 = i
                print('Soltuion 1 found: {}'.format(sol1))
        if not sol2_found:
            presents2 = scale_factor_2*sum_lazy_divisors
            if presents2 >= target:
                sol2_found = True
                sol2 = i
                print('Soltuion 2 found: {}'.format(sol2))
        if verbose and (i%1000) == 0:
            print('Calculating solutions for {}'.format(i))
        
        i += 1
    
    return (sol1, sol2)


def main():
    sol1, sol2 = get_first_houses(TARGET)
    
    print("Solution for part 1: {}".format(sol1))
    print("Solution for part 2: {}".format(sol2))


if __name__=='__main__':
    main()