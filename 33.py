def contain_like_terms(numerator, denominator):
    s_numerator = str(numerator)
    s_denominator = str(denominator)
    if s_numerator[0] == s_denominator[1] and is_not_trivial(s_numerator[0]):
        return True
    elif s_numerator[1] == s_denominator[0] and is_not_trivial(s_numerator[1]) and s_denominator[1] != "0":
        return True
    return False

def reduced(numerator, denominator):
    s_numerator = str(numerator)
    s_denominator = str(denominator)
    if s_numerator[0] == s_denominator[1]:
        return int(s_numerator[1]) / int(s_denominator[0])
    return float(s_numerator[0]) / int(s_denominator[1])

def is_not_trivial(digit):
    if digit == 0:
        return False
    return True

def main():
    for numerator in range(10,100):
        for denominator in range(numerator+1, 100):
            try:
                if contain_like_terms(numerator, denominator):
                    if reduced(numerator, denominator) == numerator/denominator:
                        print("{} / {}".format(numerator, denominator))
            except Exception as e:
                print("{} / {}".format(numerator, denominator))

print(100)