def fact(n):
    prod = 1
    for x in range(1, n + 1):
        prod *= x
    return prod

def choose(n, k):
    return fact(n) / (fact(k) * fact(n - k))


def doit():
    ans = 0
    for x in range(1, 10**2 + 1):
        for y in range(1, 10**2 + 1):
            if choose(x,y) > 10**6:
                ans += 1
    return ans
