from utils import exp_by_squaring

if __name__ == '__main__':
    big_num = 28433 * exp_by_squaring(2,7830457) + 1
    print(str(big_num)[-10:])
