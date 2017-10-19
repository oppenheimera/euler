from utils import gcd
from random import randint
from gmpy2 import is_prime
import sys

sys.setrecursionlimit(500000)

def eulers_totient(n):
    count = 0
    if is_prime(n):
        return n-1
    elif n % 2 == 0:
        return 2 * eulers_totient(n//2)
    for i in range(1,n):
        if gcd(i, n) == 1:
            count += 1
    return count

def et_to(size):
    # cache = {}
    # def et_aux(n):
    #     count = 0
    #     for i in range(1,n):
    #         if gcd(i, n) == 1:
    #             count += 1
    #     return count
    # for i in range(size):
    #     j = gcd(i, randint(1, i))
    #     if j in 
    pass

    # currmax = 0
    # n = 0
    # for i in range(1, 10**6 + 1):
    #     et_value = eulers_totient(i)
    #     if et_value > 0:
    #         temp = i / et_value
    #         if  temp > currmax:
    #             currmax = temp
    #             n = i
    # return i

def main():
    pass

main()