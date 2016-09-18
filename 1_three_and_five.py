def three_and_five(end):
    return sum([n for n in range(1, end) if n % 3 == 0 or n % 5 == 0])

def fib_gen():
    curr = 0
    next = 1
    while True:
        yield curr
        next, curr = curr + next, next

def even_fib_sum(target):
    fibs = [1]
    obj = fib_gen()
    i = 0
    while i < target + 2:
        num = next(obj)
        if num % 2 == 0 and num > 2 and num < 400000:
            fibs.append(num)
        i += 1
    return sum(fibs)
