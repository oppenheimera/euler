"""
Largest single multiplicand of a 1-9 PD-prod is 1738
"""
from gmpy2 import mul as gmp_mul
from itertools import combinations
from sys import argv

MAX = int(argv[-1])
ans = set()

def is_pandigital(a, b, n):
    l = list(str(a) + str(b) + str(gmp_mul(a, b)))
    return len(l) == n and len(set(l)) == n and '0' not in l

for t in combinations(range(2, MAX), 2):
    if is_pandigital(t[0], t[1], 9):
        print("{} * {} = {}".format(t[0], t[1], t[0] * t[1]))
        ans.add(t[0] * t[1])

print(ans)
print(sum(ans))
