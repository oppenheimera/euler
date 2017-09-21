from math import ceil
from itertools import cycle, islice, accumulate, count
"""
p(n) is a function that finds the number of partitions of a set n, where
the elements of the set are identical.

Find the smallest n for which 10^6 | p(n)

Partitions are equivalent to unique summations to n. This number is provided
by the formula: n(3n-1)/2 on the sequence 0,1,-1,2,-2,..., and is important 
to Euler's theory of partitions.

0, 1, 2, 5, 7, 12, 15, 22, 26, 35, 40, 51, 57, 70, 77, 92
0, 1, -1,2,-2, 3,  -3,  4, -4,  5, -5
0, 1, 2, 3, 4,  5,  6,  7,  8,  9, 10,

p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)+p(n-12)+p(n-15)-p(n-22)-...
"""
START = 0
BOUND = 10**7
SIGN_CYCLE = (1,1,-1,-1)
cache = {}

def gp():
    """
    >>> p = pentagonal()
    >>> [next(p) for i in range(10)]
    [1, 2, 5, 7, 12, 15, 22, 26, 35, 40]
    """
    return accumulate(k if k % 2 else k // 2 for k in count(1))


# def gp(m):
#     """ a closed formula to compute the nth generalized pentagonal number """
#     if m < 0:
#         return 0
#     elif m == 0:
#         return 1
#     elif m%2 == 0:
#         n = -m/2
#     else:
#         n = ceil(m/2)
#     return int(n*(3*n-1)/2)

def p(m):
    generalized_pents = []
    partitions = [1]
    gp_iterator = gp()
    next_gp = next(gp_iterator)
    
    yield 1
    for n in count(1):
        if next_gp <= n:
            generalized_pents.append(next_gp)
            next_gp = next(gp_iterator)
        p = sum(sign * partitions[-pent] for sign, pent in zip(
            cycle(SIGN_CYCLE), generalized_pents)) % m
        partitions.append(p)
        yield p

def get_ans(m):
    return next(i for i, p in enumerate(p(m)) if p % m == 0)

print(get_ans(10**6))
