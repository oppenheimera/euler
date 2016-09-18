from math import sqrt

def pyth_trips(n):
    lst = []
    for x in range(1,n):
        for y in range(1, n):
            if sqrt(x**2 + y**2) == sqrt(x**2 + y**2)//1:
                lst.append([x, y, int(sqrt(x**2 + y**2))])
    return lst

def sum_check(lst):
    for x in lst:
        if sum(x) == 1000:
            return x

"""
>>> f = pyth_trips(800)
>>> sum_check(f)
[200, 375, 425]
"""