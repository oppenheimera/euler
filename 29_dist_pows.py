def gen_pows(a,b):
    """all distinct combs of a^b"""
    s = set()
    for x in range(2, a + 1):
        for y in range(2, b + 1):
            s.add(x**y)
    return s