"""
find number of n-digit numbers which are also n-powers

ideas: can bound n-term by 10, and check permutations for p 
from 1 to 200
"""
from sys import argv

count = 1 # 1**1

N, P = [int(x) for x in argv[-2:]]


def is_digit_pow(n, p):
    L = len(str(n**p))
    if L == p:
        return 'eq'
    elif L > p:
        return 'gr'
    return 'le'

for n in range(1, N):
    for p in range(1, P):
        if is_digit_pow(n, p) == 'eq':
            count += 1
        elif is_digit_pow(n, p) == 'gr':
            break

print count