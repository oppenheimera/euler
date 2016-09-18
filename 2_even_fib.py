def fib_gen(mx):
    """returns a list of fibs less than mx"""
    fibs = []
    cur = 0
    nxt = 1
    while cur < mx:
        fibs.append(cur)
        cur, nxt = nxt, cur + nxt
    return fibs

def even_sum(s):
    """returns the sum of the even terms of sequence s"""
    return sum([x for x in s if x % 2 == 0])

"""
>>> even_sum(fib_gen(4000000))
4613732
"""