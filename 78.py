from math import floor
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

00000
0000 0
000 00
000 0 0 
00 00 0
00 0 0 0
0 0 0 0 0

0000
000 0
00 00
00 0 0
0 0 0 0
"""
START = 0
BOUND = 10**7

def p(m):
    """ a closed formula to compute the nth generalized pentagonal number """
    if m in [0,1]:
        return m/1
    elif m%2 == 0:
        n = m/2
    else:
        n = -floor(m/2)
    return n*(3*n-1)/2

for n in range(START + 1, BOUND):
    if p(n) % 1000000 == 0:
        print("p({}) = {}".format(n,p(n)))
        break
