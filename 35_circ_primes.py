from utils import primes
from gmpy2 import is_prime

for n in range(max(primes), 10**6, 2):
    if is_prime(n):
        primes.append(n)

def is_circ_prime(p):
    l = list(str(p))
    for i in range(1, len(l)):
        if not is_prime(int("".join(l[i:] + l[:i]))):
            return False
    return True

count = 0

for p in primes:
    if is_circ_prime(p):
        count += 1

print(count)