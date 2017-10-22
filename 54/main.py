from utils import parse_hand, Hand

def main():
    count = 0
    with open('p054_poker.txt') as f:
        for line in f:
            a,b = parse_hand(line[:-1])
            a, b = Hand(a), Hand(b)
            if a > b:
                count += 1
    print(count)
    
if __name__ == '__main__':
    main()
    