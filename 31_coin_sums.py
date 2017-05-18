"""1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)"""
import time
import sys

target = int(sys.argv[-1])

start = time.time()

def count(S, m, n):
    table = [0 for k in range(n + 1)]
    table[0] = 1
    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]
    return table[n]

denoms = (200,100,50,20,10,5,2,1)
ans = count(denoms, len(denoms), target)

elapsed = time.time() - start

print("Found {} in  {} seconds.".format(ans, elapsed))
