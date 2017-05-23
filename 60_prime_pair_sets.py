"""
>>> len(primes)
1229
"""
from utils import primes
from itertools import permutations, combinations
from gmpy2 import is_prime
from sys import argv

CUTOFF = int(argv[-1])
primes = [str(p) for p in primes]

primesets = combinations(primes[:CUTOFF], 5)
ans = [(10**6, 1)]

def prime_pairs(t):
    for pair in permutations(t, 2):
        if not is_prime(int(pair[0] + pair[1])):
            return False
    return True


for pset in reversed(list(primesets)):
    if prime_pairs(pset):
        if sum(pset) < sum(min(ans, key=sum)):
            ans.append(pset)
            print(sum(pset))
            print(pset)
            

print(sum(min(ans, key=sum)))