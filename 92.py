"""
find the number of integers below 10^6 whose "number chains" arrive at 89.

i.e. 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
"""
BOUND = 1000
count = 0

def chains_to_89(n):
    seen = [n]
    curr = n
    for i in range(BOUND):
        curr = square_digits(curr)
        if curr == 89:
            return True
        elif curr in seen:
            return False
        seen.append(curr)
    return False

def square_digits(n):
    return sum([int(char)**2 for char in str(n)])

for n in range(10**7):
    if chains_to_89(n):
        count += 1

print(count)
