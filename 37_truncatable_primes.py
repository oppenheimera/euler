"""find primes that are left and right truncatable at every stage"""
from utils import primes, prime
import time

def truncatable(n):
    p = str(n)
    trunx = [p[x:] for x in range(len(p))] + [p[:x + 1] for x in range(len(p))]
    for x in trunx:
        if not prime(int(x)) or x == '1':
            return False
    return True

def find_big(start):
    target = 0
    while target == 0:
        if prime(start) and truncatable(start):
            target = start
        start += 1
    return target

    
ans = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
