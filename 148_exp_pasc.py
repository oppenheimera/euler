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
    for x in triangle:
        print("Row {}: {}".format(i,x))
        i += 1

def check_sevens(row):
    bools = [x % 7 == 0 for x in row]
    return "Yes: {} - -  No: {}".format(bools.count(True), bools.count(False))

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

def calculate_seq(hi):
    total = 0
    seq_start = 1
    i = 1
    while i < hi:
        for x in range(1,8):
            total += seq_start * x
            i += 1
        seq_start += 1
    return total


elapsed = start - time.time()


