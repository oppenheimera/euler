from gmpy2 import is_prime
from itertools import combinations
from sys import argv

def work(l, i):
    """
    :param l: the length of primes desired
    :param i: the indices to be replaced with asterixes
    
    returns all eight-family primes (if any exist) of
    length-l primes where all indices i are equal
    """
    d = dict()
    candidates = [x for x in n_length_primes(l)]
    candidates = [[x for x in y] for y in candidates if checkindices(y, i)]
    for c in candidates:
        for idx in i:
            c[idx] = '*'
    candidates = [''.join(x) for x in candidates]
    for x in candidates:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    eight_fams = [key for key in d if d[key] == 8]
    return eight_fams 

def checkindices(p, i):
    """
    :param p: prime to be checked
    :param i: indices to be checked

    >>> checkindices('121313', (0,2,4))
    True
    """
    assert type(p) == str, "argument p is not a string"
    for idx in i[1:]:
        if p[idx] != p[i[0]]:
            return False
    return True

def n_length_primes(n):
    """ Returns all primes of length n as strings. """
    assert n > 0, "Cannot generate a list of %d length primes." % n
    a = []
    for i in range(10**(n-1), 10**n):
        if is_prime(i):
            a.append(str(i))
    return a

def findfamily(p):
    """
    given an 'asterixed' prime, find its family.

    >>> findfamily('121313'):
    ['121313', '222323', '323333', '424343', '525353', '626363', '828383', '929393']
    """
    ans = []
    for i in range(10):
        candidate = p.replace("*", str(i))
        if is_prime(int(candidate)):
            ans.append(candidate)
    return sorted(ans)

def findsolutions(r, l):
    """
    :param r: length of primes desired
    :param l: number of indices to check

    i.e. main(5, 2) checks length five primes at every
    two possible indicies
    """
    ans = []
    for c in combinations(range(r), l):
        ans += work(r, c)
    return sorted(ans)

def main(r, l):
    for sol in findsolutions(r, l):
        print(findfamily(sol))

if __name__ == '__main__':
    r, l = argv[-2:]
    main(int(r), int(l))
