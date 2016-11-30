import time
from itertools import combinations

upperbound = 28123

def factors(n):
    res = set([1])
    for x in range(2, n//2):
        if n%x == 0:
            res.add(x)
            res.add(n//x)
    return res

def abundant(n):
    if sum(factors(n)) > n:
        return True
    return False

def perfect(n):
    if sum(factors(n)) != n:
        return False
    return True

def build_list():
    res = []
    for x in range(1, upperbound):
        if abundant(x):
            res.append(x)
    return res

def make_combs(l, r=2):
    return list(combinations(l,r))

def test_combs(c):
    res = []
    for tup in c:
        if sum(tup) < upperbound:
            res.append(tup[0])
            res.append(tup[1])
    return res 
ls