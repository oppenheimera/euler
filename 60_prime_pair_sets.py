from utils import p as primes
from itertools import permutations, combinations
from gmpy2 import is_prime
from sys import argv
"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two 
primes and concatenating them in any order the result will always be 
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set 
of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.
"""
big_prime_dict = dict()

def satifsfies_prime_pairings(tup):
    if '5' in tup or '2' in tup:
        return False
    
    pset = set()
    
    for p in permutations(tup, 2):
        a, b = p
        pset.add(int(a + b))
    for N in pset:
        if N in big_prime_dict:
            if big_prime_dict[N] == False:
                return False
            return True
        elif N not in big_prime_dict:
            if divides_three(N) == True:
                big_prime_dict[N] = False
            elif divides_nine(N) == True:
                big_prime_dict[N] = False
            elif is_prime(N) == False:
                big_prime_dict[N] = False
            else: 
                big_prime_dict[N] = True
    return big_prime_dict[N]

def digit_sum(N):
    i = 0
    for s in str(N):
        i += int(s)
    return i

def get_sum(tup):
    """
    Returns digit sum of tuples, accepts both strings an integers
    """
    i = 0
    if type(tup[0]) == int:
        for n in tup:
            i += n
    elif type(tup[0]) == str:
        for s in tup:
            i += int(s)
    return i        

def divides_three(n):
    if n ==3: 
        return True
    if digit_sum(n) % 3 == 0:
        return True
    return False

def divides_nine(n):
    if n == 9:
        return True
    if digit_sum(n) % 9 == 0:
        return True
    return False

if argv[-1] == 'debug':
    for l in range(3,300,3):
        if not divides_three(l):
            print("Errored in {}-batch on {}".format(3,l))
    for n in range(9,900,9):
        if not divides_nine(n):
            print("Errored in {}-batch on {}".format(9,n))
    print("Successfully ran {} divisor test cases".format(300*900))
    if satifsfies_prime_pairings(('3', '7', '109', '673')) == False:
        print('satifsfies_prime_pairings is broken')
    print("satifsfies_prime_pairings is working")

if argv[-1] == 'run':
    primes = [str(p) for p in primes]

    primesets = combinations(primes, 5)
    ans = [(10**6, 1)]

    for pset in primesets:
        if satifsfies_prime_pairings(pset):
            if get_sum(pset) < get_sum(min(ans, key=get_sum)):
                ans.append(pset)
                print("Found set {} summing to {}.".format(pset, get_sum(pset)))
            
