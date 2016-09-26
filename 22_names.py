import re, time
start = time.time()

f = open('names.txt', 'r')
score = dict((k,v) for v,k in list(enumerate([x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'], 1)))
lst = sorted(re.findall(r'"(.*?)"', f.read()))

ans = sum(map(lambda n: sum([score[x] for x in lst[lst.index(n)]]) * (lst.index(n) + 1), lst))
f.close()
elapsed = time.time() - start

print("Found answer {} in {} seconds.".format(ans, elapsed))