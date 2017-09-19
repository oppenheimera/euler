from utils import prime
from math import sqrt
"""
65 64 63 62 61 60 59 58 57
66 37 36 35 34 33 32 31 56
67 38 17 16 15 14 13 30 55
68 39 18  5  4  3 12 29 54
69 40 19  6  1  2 11 28 53
70 41 20  7  8  9 10 27 52
71 42 21 22 23 24 25 26 51
72 43 44 45 46 47 48 49 50
73 74 75 76 77 78 79 80 81

key observation: bottom right diagonals are odd squares 

We'll use the notation 
d1 d2
d3 d4
to denote diagonals 1,2,3, and 4.

d4 = some odd 'n' squared
d3 = d4 - (sqrt(d4) - 1)
d2 = d4 - 2 * (sqrt(d4) - 1)
d1 = d4 - 3 * (sqrt(d4) - 1)

At this point the code writes itself.
"""
side_len = 1
prime
def get_percent_prime(l):
    return len([p for p in l if prime(p)]) / len(l)

def get_diags(d4):
    l = [d4]
    l += [d4 - n * (sqrt(d4) - 1) for n in range(1,4)]
    return l

idx = 3
number_of_primes = 3
number_of_diags = 5

while number_of_primes / number_of_diags > .1 and number_of_primes != 0:
    print(number_of_primes / number_of_diags)
    number_of_primes += sum([True for p in get_diags(idx**2) if prime(p)])
    number_of_diags += 4
    idx += 2

print("d4: {}; len(side): {}".format((idx-2)**2, idx))