def is_palindrome(n):
    n_as_str = str(n)
    return n_as_str == str(reverse(n_as_str))

def reverse(n):
    s = str(n)
    new_s = ""
    for n in range(1, len(s) + 1):
        new_s += s[n * -1]
    return int(new_s)

def is_lychrel(n, iterations):
    if iterations == 0:
        return True
    else:
        left = n
        right = reverse(n)
        lychrel_sum = left + right
        if is_palindrome(lychrel_sum):
            return False
        else:
            return is_lychrel(lychrel_sum, iterations - 1)

def get_lychrels_below(n):
    count = 0
    for candidate in range(n):
        if is_lychrel(candidate, 50):
            count += 1
    return count

print(get_lychrels_below(10000))