import traceback

"""
If all the numbers from 1 to 1000 (one thousand) inclusive 
were written out in words, how many letters would be used?
>>> nums_two([str(x) for x in range(1,1001)])
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
    '7':len('sevenhunred'), '8':len('eighthundred'), '9':len('ninehundred')}
quads = {'1000': len('onethousand')}

def number():
    count = 0
    for a in singles.values():
        count += a * 100
    for b in doubles.values():
        count += b * 10
    for c in do_build.values():
        count += c * 100
    for d in triples.values():
        count += d * 100
    for e in quads.values():
        count += e
    return count

def nums_two(lst):
    count = 0
    try:
        for x in lst:
            if len(x) == 1:
                count += singles[x]
            if len(x) == 2:
                if x in doubles:
                    count += doubles[x]
                else:
                    count += singles[x[1]]
                    count += do_build[x[0]]
            if len(x) == 3:
                if x[1:] != '00':
                    count += 3
                if x[1:] in doubles:
                    count += doubles[x[1:]]
                    count += triples[x[0]]
                else:
                    count += singles[x[2]]
                    count += do_build[x[1]]
                    count += triples[x[0]]
            if len(x) == 4:
                count += quads[x]
    except KeyError as k:
        traceback.print_exc()
        print("errored out on: " + str(x))
    print("counted " + str(count) + " letters")
    return