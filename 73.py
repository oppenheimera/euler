from gmpy2 import gcd

LOW_BOUND = 1/3
HIGH_BOUND = 1/2
D = 12000
count = 0

for numerator in range(1,D + 1):
    for denominator in range(numerator,D + 1):
        n = numerator/denominator
        if n > LOW_BOUND and n < HIGH_BOUND and int(gcd(numerator, denominator)) == 1:
            count += 1
        elif n < LOW_BOUND:
            break
print(count)