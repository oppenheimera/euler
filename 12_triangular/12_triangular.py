from math import gcd
"""
500 == 2 * 2 * 5 * 5 * 5
a_1 = 2 - 1
a_2 = 2 - 1
a_3 = 5 - 1
a_4 = 5 - 1
a_5 = 5 - 1
So number must be in the form n_1^(a_1) n_2^(a_2) n_3^(a_3) n_4^(a_4) n_5^(a_5),
or 'a b c**4 d**4 e**4' such that abcde are unique primes that minimize eqn.
Giving us 7 * 11 * 2**4 * 3**4 * 5**4
"""

def divisors(n):
    divs = set()
    for x in range(1,n//2):
        if n % x == 0:
            divs.add(x)
    return len(divs)

def pollards_rho(n):
    x, y, d = 2, 2, 1
    g = lambda y: (y**2 - 1) % n
    while d == 1:
        x = g(x)
        y = g(g(y))
        d = gcd(abs(x - y), n)
    if d == n:
        return 'Failure'
    else: 
        return d

tri = lambda x: sum([n for n in range(x+1)])
