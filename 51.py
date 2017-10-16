from gmpy2 import is_prime
from sys import argv

def n_length_primes(n):
    """ Returns all primes of length n as strings. """
    assert n > 0, "Cannot generate a list of %d length primes." % n
    a = []
    for i in range(10**(n-1), 10**n):
        if is_prime(i):
            a.append(str(i))
    return a

def find(string, target):
    return [i for i in range(len(string)) if string[i] == target]

def get_fam(base):
    indices = find(base, "*")
    found = []
    primes = n_length_primes(len(base))
    for p in primes:
        if indices_eq(p, indices) and base_eq(base, p):
            found.append(p)
    return found

def indices_eq(string, indices):
    """
    :param string: base string to check
    :param indices: indices that need be checked.

    Returns a boolean dictating whether all indices of the string are 
    of the same character.

    >>> indices_eq("56003", [2,3])
    True
    """
    targ = string[indices[0]]
    for i in indices[1:]:
        if string[i] != targ:
            return False
    return True

def base_eq(string1, string2):
    """
    :param string1: the base string, should be of the form '123**67'.
    :param string2: the string which is to be evaluated against string1

    Returns a boolean dictating whether string1 and string2 contain the 
    same characters, outside of all '*' characters

    >>> base_eq('56**3', '56003')
    True
    """
    assert '*' in string1, "Bad argument, string1 (%d) must contain the character '*'." % string1
    for i in range(len(string1)):
        if string1[i] != '*' and string1[i] != string2[i]:
            return False
    return True


def edits_away(string1, string2):
    return sum([1 for i in range(len(string1)) if string1[i] != string2[i]])

def primes_with_n_subs(n, edits, targ):
    """
    :param n: length of primes being checked.
    :param edits: substitution distance allowed.
    :param targ: size of family desired.
    """
    primes = n_length_primes(n)
    macro_ans = []
    try:
        for i in range(len(primes)):
            ans = [primes[i]]
            for j in range(i, len(primes)):
                if edits_away(primes[i], primes[j]) == edits:
                    ans.append(primes[j])
            if len(ans) == targ:
                macro_ans.append(ans)
                for elem in ans:
                    primes.remove(elem)
    finally:
        return macro_ans

def main(s):
    """
    :param s: the base string to be checked.

    Command line argument should be of the form: 
    $ python 51.py 's'
    """
    ans = get_fam(s)
    print(len(ans), ans)

if __name__ == '__main__':
    arg = argv[-1]
    # main(arg)
