from sys import argv
from gmpy2 import mul

BEGIN, END = [int(x) for x in argv[-2:]]

def check_eq(n):
    s = sorted(list(str(2*n)))
    for i in range(3,7):
        if sorted(list(str(mul(i, n)))) != s:
            return False
    return True

def main(a, b):
    for n in range(a, b):
        if check_eq(n):
            return n

print(main(BEGIN, END))