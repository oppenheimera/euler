from itertools import combinations
from math import ceil
""" 
Find the sum of all positive integers which cannot be represented as the
sum of any 3 unique generalized pentagonal numbers.
"""

def gp(m):
    """ Computes the nth generalized pentagonal number
    >>> [gp(n) for n in range(10)]
    [0, 1, 2, 5, 7, 12, 15, 22, 26, 35]
    """
    if m == 0:
        return 0
    elif m%2 == 0:
        n = -m/2
    else:
        n = ceil(m/2)
    return int((3*n**2 - n)/2)

def get_ans(m=33067):
    pents = [gp(n) for n in range(m)]
    arr = [True]*m
    for tup in combinations(pents,3):
        if sum(tup) < m:
            arr[sum(tup)] = False
    return sum(arr)

# print(get_ans())

def can_be_spelled(word, arr):
    for char in set(word):
        if word.count(char) > arr.count(char):
            return False
    return True

def longest(words, chars):
    curr_longest = ''
    for word in words:
        if can_be_spelled(word, chars) and len(word) > len(curr_longest):
            curr_longest = word
    return curr_longest
import re

page = open('untitled.html', 'r').read()
# re.match(r"^.*\['(.*)'\].*$",page)
