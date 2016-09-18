def ten_div(n):
    muls = [6,7,8,9,10]
    # for x in range(1,11):
    for x in muls:
        if n % x != 0:
            return False
    return True

def twenty_div(n):
    muls = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # for x in range(1,21):
    for x in muls:
        if n % x != 0:
            return False
    return True

def find_div(f, m=10000):
    """f is a div test func"""
    i = 20
    while i < m:
        if f(i):
            return i
        i += 1

"""
>>> find_div(ten_div, 10**10)
2520
>>> find_div(twenty_div, 10**10)
232792560
"""