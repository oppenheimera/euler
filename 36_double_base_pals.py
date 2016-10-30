"""Find all n < 10**2 which are palindromic in binary and b_10"""
import time

start = time.time()

def is_pal(str):
    pivot = len(str) // 2
    if len(str) % 2 == 1:
        front = str[:pivot]
        back = str[pivot + 1:]        
    else:
        front = str[:pivot]
        back = str[pivot:]
    return front == back[::-1]

def doit(upper):
    total = 0
    for n in range(1, upper):
        if is_pal(str(n)) and is_pal((bin(n)[2:])):
            total += n
    return total

ans = doit(10**6 + 1)
elapsed = time.time() - start

print("Found {} in {} seconds.".format(ans, elapsed))
