from itertools import product
import time

start = time.time()

def pattern(n):
    l = [x for x in str(n)][::2]
    if all(int(l[x-1]) == x for x in range(1,10)):
        return True
    return False


start = 138902663    # sqrt(19293949596979899)
while not pattern(start**2):
    start -= 1

elapsed = time.time() - start

print("found ans: {} in {} seconds".format(start * 10 , elapsed))
