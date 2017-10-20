def makerules(string):
    s = set()
    for i in range(len(string)-1):
        s.add("{} -> {}".format(string[i], string[i+1]))
    return s

def main():
    s = set()
    with open('p079_keylog.txt') as f:
        for line in f:
            for rule in makerules(line[:-1]):
                s.add(rule)
    for x in sorted(s):
        print(x)

if __name__ == '__main__':
    main()
