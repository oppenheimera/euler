count = 0
BOUND = 1000

for n in range(1,BOUND):
    for p in range(1,BOUND):
        if len(str(n**p)) == p:
            count += 1
        else:
            break
print(count)