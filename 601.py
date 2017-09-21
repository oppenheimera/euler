from itertools import count
def streak(n):
    """ Returns the divisibility streak of n
    13 is divisible by 1 
    14 is divisible by 2 
    15 is divisible by 3 
    16 is divisible by 4 
    17 is NOT divisible by 5 
    So streak(13)=4.

    >>> streak(13)
    4
    """
    for i in count(0):
        if (n+i) % (i+1) != 0 or (i+1) > n:
            return i

def P(s, N):
    """ The number of integers n, 1 < n < N, for which streak(n) = s.
    >>> P(3,14)
    1
    >>> P(6,10**6)
    14286
    """
    count = 0
    for n in range(1, N+1):
        if streak(n) == s:
            count += 1
    return count

def get_ans():
    count = 0
    for i in range(1, 32):
        count += P(i, 4**i)
    return count

print(get_ans())
