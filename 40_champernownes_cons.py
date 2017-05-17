"""
find prod d_10**0...d_10**6
"""

champernownes = ""
for n in range(1, 1000000):
    champernownes += str(n)

ans = 1
for n in range(6):
    ans *= int(champernownes[10**n - 1])

print ans