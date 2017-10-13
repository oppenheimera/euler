from sys import argv
from gmpy2 import mpz, isqrt, is_prime

def factors(n):
    result = set()
    n = mpz(n)
    for i in range(1, isqrt(n) + 1):
        div, mod = divmod(n, i)
        if not mod:
            result |= {mpz(i), div}
    return result

def prime_factorize(n):
    pfs = {i for i in factors(n) if is_prime(i)}
    improved_pfs = set()
    for f in pfs:
        improved_pfs.add(power_case(f, n))
    return improved_pfs

def power_case(f, n):
    """
    Finds largest factor of form f^i such that f^i divides n.
    """
    i = 1
    while f**i < n and n % f**i == 0:
        i += 1
    return f**(i-1)

def distinct_prime_factors(n, r):
    superset = set()
    for i in range(r):
        superset = superset.union(prime_factorize(n + i))
    return len(superset) >= r**2

def main(factors):
    i = 1
    while not distinct_prime_factors(i, factors):
        i += 1
    print(i)

if __name__ == '__main__':
    arg = int(argv[-1])
    main(arg)