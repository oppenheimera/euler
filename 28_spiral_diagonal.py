from math import ceil
from sys import argv

n = int(argv[-1])

def get_outer_diags(n):
    s = n**2
    if n == 1:
        return 1
    return sum([s - ((s**(1/2)-1)*m) for m in range(4)])

print(sum([get_outer_diags(i) for i in range(1, n+1, 2)]))
