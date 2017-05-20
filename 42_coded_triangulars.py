"""
max sum word is 'responsibility', at value 192
only need to look at tris < 192
"""
from math import sqrt
words = open('words.txt', 'r').read().replace('"', '').lower().split(',')
tups = enumerate('abcdefghijklmnopqrstuvwxyz', 1)
tris = [n*(n+1)/2 for n in range(21)]
keys = dict()
count = 0

def sum_chars(word):
    return sum([keys[char] for char in word])

for t in tups:
    keys[t[1]] = t[0]

for word in words:
    if sum_chars(word) in tris:
        count += 1

print count