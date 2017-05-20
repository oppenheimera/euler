"""
sum of prime and 2x a square
"""
from utils import primes, prime

p2sq = set()

for p in primes:
    for n in range(1,len(primes)):
        p2sq.add(p + 2 * n**2)

odd_composites = [n for n in range(3, max(p2sq), 2) if not prime(n)]

def doit():
    for n in odd_composites:
        if n not in p2sq:
            return n

print doit()