"""
T(285) = P(165) = H(143) = 40755

tris end in '1', '0', '3', '5', '6', '8'
pents end in '1', '0', '2', '5', '7', '6'
hexs end in '1', '0', '3', '5', '6', '8'
common numbers must end in '1', '0', '5', '6'

UPDATE: All triangle numbers are hexagonal as well, making looking
at triangular numbers superfluous. Speedup by comparing only hexs to pents
"""
from sys import argv

UPPERBOUND = int(argv[-1])

T = lambda n: n * (n + 1) / 2
P = lambda n: n * (3*n - 1) / 2
H = lambda n: n * (2*n - 1)
common = ['1', '0', '5', '6']

tris = [T(n) for n in range(1000, UPPERBOUND) if str(T(n))[-1] in common]
pents =  [P(n) for n in range(166, UPPERBOUND) if str(P(n))[-1] in common]
hexs = [H(n) for n in range(144, UPPERBOUND) if str(H(n))[-1] in common]

def recursive_binary_search(A, target):
    i = len(A)//2
    if i == 1 and A[i] != target:
        return False
    elif A[i] == target:
        return True
    elif A[i] > target:
        return recursive_binary_search(A[0:i+1], target)
    else:
        return recursive_binary_search(A[i:], target)

for n in tris:
    if recursive_binary_search(pents, n) and recursive_binary_search(hexs, n):
        print n
print "Didn't find anything"
