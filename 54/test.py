from utils import parse_hand, Hand

def main():
    with open('testfile.txt') as f:
        for line in f:
            a,b = parse_hand(line[:-1])
            a, b = Hand(a), Hand(b)
            print(a > b)

if __name__ == '__main__':
    main()