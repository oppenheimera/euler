from math import log
"""
requisite knowledge: log_a(x^y) = y*log_a(x)
"""

def read_in():
    ans = []
    f = open('p099_base_exp.txt', 'r')
    for line in f:
        pair = [int(i) for i in line[:-1].split(',')]
        ans.append(tuple(pair))
    return ans

def get_magnitude(tup):
    base, exp = tup
    return exp * log(base)

def main():
    base_exp_pairs = read_in()
    currmax = get_magnitude(base_exp_pairs[0])
    index_of_currmax: 0
    for i in range(1, len(base_exp_pairs)):
        candidate = get_magnitude(base_exp_pairs[i])
        if candidate > currmax:
            currmax = candidate
            index_of_currmax = i
    print(candidate, index_of_currmax + 1)

if __name__ == '__main__':
    main()