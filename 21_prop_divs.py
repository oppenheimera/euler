import time

start = time.time()
div = lambda x: [y for y in range(1, x//2+1) if x%y == 0]


def get_it(n):
    answers = set()
    for x in range(1, n):
        n = sum(div(x))
        if sum(div(n)) == x and n != x:
            answers.add(x)
    return answers

a = sum(get_it(10000))
elapsed = time.time() - start

print("The sum of the amicables under 10000 is {}. \
    I found this answer in {} seconds".format(a, elapsed))