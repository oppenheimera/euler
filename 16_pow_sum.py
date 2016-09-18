def do_sum(n):
    count = 0
    for x in str(n):
        count += int(x)
    return count

do_sum(2**100)
