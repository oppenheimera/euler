import time, math
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
f = 7 * 11 * 2**4 * 3**4 * 5**4
tr = lambda n: [sum(range(x)) for x in range(n)]
def divisors(n):
    divs = set([1,n])
    for x in range(1,n):
        if n % x == 0:
            divs.add(x)
    return len(divs)

def n_divisors(n):   
    divs = 1
    for x in range(1, n // 2):
        if x  == math.sqrt(n):
            divs += 1
        elif n % x == 0:
            divs += 2
    return divs

def doit(start):
    for x

def test(fn, val):
    start = time.time()
    ans = fn(val)
    elapsed = time.time() - start
    print(ans)
    return elapsed
