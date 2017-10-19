from itertools import combinations
from utils import gcd

def satisfies_constraints(tup):
    numerator, denominator = tup
    if gcd(numerator, denominator) == 1 and numerator < denominator:
        return True
    return False

def main():
    reduced_pfs = []
    for comb in combinations(range(1, 10**6 + 1), 2):
        if satisfies_constraints(comb):
            reduced_pfs.append(comb)
    reduced_pfs.sort(key=lambda tup: tup[0] / tup[1])
    i = reduced_pfs.index((3,7))
    print(reduced_pfs[i-1])

main()