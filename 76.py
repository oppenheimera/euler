"""
0000 0 
000 00
000 0 0
00 00 0
00 0 0 0
0 0 0 0 0
"""
TARGET = 100

def count(S, m, n):
    table = [0 for k in range(n + 1)]
    table[0] = 1
    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]
    return table[n]

def get_ans(t):
    denoms = [n for n in range(1, t)]
    return count(denoms, len(denoms), t)

print(get_ans(TARGET))
