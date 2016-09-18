from itertools import *
import time

start  = time.time()

p = list(permutations([str(x) for x in range(10)]))
perms = []

for x in p:
    perms.append(int(''.join(x)))

sorted(perms)
elapsed = time.time() - start

print("The millionth (1 indexed) sorted permutation is {}.".format(perms[10**6 - 1]))
print("Found an answer in: {} seconds.".format(elapsed))


"""
The millionth sorted permutation is 2783915460.
Found an answer in: 4.33597993850708 seconds.
"""