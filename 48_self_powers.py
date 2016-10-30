def series(n):
    su = 0
    for x in range(1, n + 1):
        su += x**x
    return su

ans = series(1000)

print("Answer is {}".format(str(ans)[-10:]))