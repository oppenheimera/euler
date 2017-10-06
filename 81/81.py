import sys
sys.path.append('/Users/oppenheimer/broject_euler')
from utils import matrix

M = [131,673,234,103,18,201,96,342,956,150,630,803,746,422,111,537,699,497,121,956,805,732,524,37,331]

def read_matrix(path='matrix.txt'):
    m = []
    for line in open(path, 'r').read():
        m.append(line.split())

def get_path(M):
    A = matrix(M.size)
    s = 0
    for i in range(M.size): # set up A_{0,i}
        s += M.at(0, i)
        print("s: {}, coords:({},{})".format(s, 0, i))
        A.put(0, i, s)
    # s = 0
    # for j in range(M.size): # set up A_{i, 0}
    #     s += M.at(i, 0)
    #     A.put(i, 0, s)
    A.pprint()

M = matrix(int(len(M)**(1/2)), M)
get_path(M)
