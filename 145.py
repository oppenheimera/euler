from sys import argv

def revsum(s):
    assert type(s) == str, "Bad argument, s is not of type str"        
    return str(int(s) + int(s[::-1]))

def all_odd(s):
    assert type(s) == str, "Bad argument, s is not of type str"
    for char in s:
        if int(char) % 2 == 0:
            return False
    return True

def main(bound):
    count = 0
    for i in range(1, bound):
        if i % 10 != 0:
            if all_odd(revsum(str(i))):
                count += 1
    print(count)

if __name__ == '__main__':
    bound = int(argv[-1])
    main(bound)