def collatz(n):
    i = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        i += 1
    return i

def collatzeral(lim):
    dic = {}
    for x in range(1, lim + 1):
        dic[collatz(x)] = x
    return dic

"""
>>> ans = collatzeral(10**6)
>>> ans[max(ans)]
837799
"""