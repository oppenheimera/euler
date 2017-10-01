from gmpy2 import is_prime
from itertools import permutations

N = 9
candidates = list(permutations(range(1,N), N-1))

def concatenate_digits(t):
    s = ""
    for n in t:
        s += str(n)
    return int(s)

def get_ans():
    for t in candidates[::-1]:
        if is_prime((concatenate_digits(t))):
            return concatenate_digits(t)

print(get_ans())
