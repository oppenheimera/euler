"""
Find the maximum "digital sum" for a number a^b, where a,b < 100
"""
largest_sum = 0
a, b = 0, 0

def digital_sum(n):
    return sum([int(char) for char in str(n)])

for i in range(1,100):
    for j in range(1,100):
        temp = digital_sum(i**j)
        if temp > largest_sum:
            largest_sum = temp
            a, b = i, j
print("a:{}, b: {}, digital_sum(a**b): {}".format(a,b,largest_sum))
