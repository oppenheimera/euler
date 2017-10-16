from utils import primes
from itertools import permutations, combinations
from gmpy2 import is_prime

#673
BASE_SET = {'3', '7', '109', '673'}
primes.remove(5)
primes.remove(2)
primes = [str(p) for p in primes]

def find_missing_elem(s):
    for p in primes:
        if p not in s and satisfies_pairing(s, p):
            s.add(p)
            print(s, sum(s))
            return


def satisfies_pairing(s, p):
    """
    :param s: a set of primes as strings
    :param p: a prime as a string
    
    Returns a boolean indicating whether p concatenates successfully in
    any order to the primes in s
    
    >>> satisfies_pairing({'3', '7', '109'}, '673')
    True
    """
    s_copy = s.copy()
    s_copy.add(p)
    for t in permutations(s_copy, 2):
        candidate = int(''.join(t))
        if is_prime(candidate) == False:
            return False
    return True

def main():
    for comb in combinations(primes, 4):
        find_missing_elem(set(comb))


if __name__ == '__main__':
    main()