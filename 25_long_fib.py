import time

start = time.time()

def fib_dynamic(n):
    a, b  = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def find_long_fib(target):
    a = 0
    f = lambda x: len(str(x))
    while f(fib_dynamic(a)) != target:
        a += 1
    return (a, fib_dynamic(a))

ans = find_long_fib(1000)
elapsed = time.time() - start
print("The index of the requested length Fibonacci number is: " + str(ans[0]))
print("I found an answer in: " + str(elapsed)) 

"""
The index of the requested length Fibonacci number is: 4782
I found an answer in: 2.0899500846862793
"""