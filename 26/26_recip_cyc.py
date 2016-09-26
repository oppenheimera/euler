from itertools import groupby
import time

# start = time.time()

def func(n):
    ans = []
    for x in range(1,n): 
        groups = groupby(str(1/x))
        result = [(label, sum(1 for _ in group)) for label, group in groups]
        ans.append((x, max(result)))
    return ans

def find_max(lst):
    curr_max = 0
    curr_max_count = 0
    for x in lst:
        if x[1][1] > curr_max_count:
            curr_max_count = x[1][1]
            curr_max = x[0]
    return (curr_max, curr_max_count)

# ans = find_max(func(1000))
# elapsed = time.time() - start

f = open('abc.txt', 'w')
for x in range(1,1000):
    f.write("{}: {}\n".format(x, str(1/x)))

# print("Found answer 1/{} = {} in {} seconds.".format(ans[0], ans[1], elapsed))