import time
start = time.time()

triangle = open('67triangle.txt', 'r')

def parse():
    tree = []
    line = triangle.readline()
    while line != '':
        tree.append([int(x) for x in line.split()])
        line = triangle.readline()
    return tree

def check_children(lvl):
    sequence = []
    for i in range(len(t[lvl])):
        l_path = t[lvl + 1][i]
        r_path = t[lvl + 1][i + 1]
        c_node = t[lvl][i]
        if c_node + r_path >= c_node + l_path:
            t[lvl][i] = c_node + r_path
        else:
            t[lvl][i] = c_node + l_path

def do_stuff():
    for i in range(len(t) - 1)[::-1]:
       check_children(i)

t = parse()
do_stuff()
elapsed = time.time() - start
print("Found an answer in: {} seconds.".format(elapsed))
print("The answer is: {}.".format(t[0][0]))