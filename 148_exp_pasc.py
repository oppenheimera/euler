import time
from math import sqrt, floor

"""
Pattern is that the numbers which aren't divisible by 7 are summations
from n, stepping by n, for seven iterations
"""

start = time.time()

def tri_constructor(n):
    #  makes two extra rows
    triangle = [[1]]
    while n >= 0:
        triangle.append([get_val(x, triangle[-1]) for x in range(0, len(triangle[-1]) + 1)])
        n -= 1
    return triangle

def get_val(x, prev_row):
    if x == 0 or x == len(prev_row):
        return 1 
    else:    
        return prev_row[x] + prev_row[x - 1]
  
def pretty_print(triangle):
    i = 0
    for row in triangle:
        r = []
        for col in row:
            if col % 7 == 0:
                r.append(1)
            else: 
                r.append(0)
        print(r)

def check_sevens(row):
    bools = [x % 7 == 0 for x in row]
    return "Yes: {} - -  No: {}".format(bools.count(True), bools.count(False))

def stats(n):
    for x in n:
        print("{} -> {}".format((len(x) - 1), check_sevens(x)))

def check(tri):
    entries = 0
    count = 0
    for row in tri:
        for col in row:
            entries += 1
            if col % 7 != 0:
                count += 1
    return "({} / {})".format(count, entries)

def cheat(n):
    if n < 7:
        return 0
    elif n % 7 == 0:
        return n - floor(sqrt(n)) + 1
    else:
        lm = last_multiple(n)
        return cheat(lm) - (n-lm) * (floor(sqrt(lm)) - 1)

def last_multiple(n):
    while n % 7 != 0:
        n -= 1
    return n

f = lambda n: [x for x in range(n, n * 7 + 1, n)]

def no(n):
    return (n - last_multiple(n) + 1) * (n // 7 + 1)


elapsed = start - time.time()


