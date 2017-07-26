import sys
"""
If all the numbers from 1 to 1000 (one thousand) inclusive 
were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 
342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance 
with British usage.
"""


singles = {'0': 0,'1': len('one'), '2':len('two'), '3':len('three'), '4':len('four'),
    '5':len('five'), '6':len('six'), '7':len('seven'), '8':len('eight'), '9':len('nine')}
doubles = {'10':len('ten'), '11':len('eleven'), '12':len('twelve'), '13':len('thirteen'),
    '14':len('fourteen'), '15':len('fifteen'), '16':len('sixteen'), '17':len('seventeen'),
    '18':len('eighteen'), '19':len('nineteen')}
do_build = {'0': 0,'2':len('twenty'), '3':len('thirty'), '4':len('forty'), '5':len('fifty'),
    '6':len('sixty'), '7':len('seventy'), '8':len('eighty'), '9':len('ninety')}
triples = {'1':len('onehundred'), '2':len('twohundred'), '3':len('threehundred'), 
    '4':len('fourhundred'), '5':len('fivehundred'), '6':len('sixhundred'), 
    '7':len('sevenhundred'), '8':len('eighthundred'), '9':len('ninehundred')}
quads = {'1000': len('onethousand')}

def get_sum(NUM):
    N = str(NUM)
    if NUM < 100:
        if NUM < 10:
            return singles[N]
        elif NUM < 20:
            return doubles[N]
        return do_build[N[0]] + singles[N[1]]
    elif NUM < 1000:
        if NUM % 100 == 0:
            return triples[N[0]]
        elif NUM % 100 < 10:
            return triples[N[0]] + len("and") + singles[N[2]]
        elif NUM % 100 < 20:
            return triples[N[0]] + len("and") + doubles[N[1:]]
        return triples[N[0]] + len('and') + do_build[N[1]] + singles[N[2]]
    elif NUM == 1000:
        return quads[N]

def test(S):
    return len(S.replace(" ", ""))

#test cases
if len(sys.argv) >= 2:
    if sys.argv[-1].lower() == 'debug':
        assert get_sum(342) == 23
        assert get_sum(115) == 20
        assert sum([get_sum(n) for n in range(1,6)]) == 19
        assert get_sum(301) == test("three hundred and one")
        assert get_sum(111) == test("one hundred and eleven")
        assert get_sum(65) == test("sixty five")
        assert get_sum(555) == test("five hundred and fifty five")
else:        
    ANSWER = sum([get_sum(n) for n in range(1, 1001)])
    print("Answer is {}".format(ANSWER))
