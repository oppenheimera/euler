def is_pandigital(s):
    """
    Return a boolean ascerting whether string s is pandigital or not.
    """

    try:
        return all([len(s) == 9, set(s) == set('123456789')])
    except TypeError as te:
        class_name = type(s).__name__
        print("TypeError: bad operand type for is_pandigital(): '{}'".format(class_name))

def make_multiple(n, r):
    """
    Returns the concatenated product of n * r_0 + ... + n * r_m 

    param: r is inclusive and begins at 1
    """
    assert type(n) == int
    assert type(r) == int
    return ''.join([str(n * i) for i in range(1, r+1)])

def main():
    c_max = 0
    for n in range(10000):
        for r in range(10):
            p = make_multiple(n, r)
            if is_pandigital(p):
                if int(p) > c_max:
                    c_max = int(p)
            if len(p) > 9:
                break
    print(c_max)


if __name__ == '__main__':
    main()
