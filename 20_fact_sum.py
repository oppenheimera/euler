from math import factorial

def do_sum(n):
    count = 0
    for x in str(n):
        count += int(x)
    return count

print(do_sum(factorial(100)))