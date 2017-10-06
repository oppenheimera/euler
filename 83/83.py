import sys
sys.path.append('/Users/oppenheimer/broject_euler')
from utils import matrix

M = [131,673,234,103,18,201,96,342,956,150,630,803,746,422,111,537,699,497,121,956,805,732,524,37,331]
M = matrix(5, M)

def read_matrix(path='matrix.txt'):
    ans = []
    for line in open(path, 'r'):
        l = [int(i) for i in line[:-1].split(',')]
        ans += l
    return ans

def get_path(M):
    A = matrix(M.size)
    s = 0
    for i in range(M.size): # set up A_{0,i}
        s += M.at(0, i)
        A.put(0, i, s)
    s = 0
    for j in range(M.size): # set up A_{i, 0}
        s += M.at(j, 0)
        A.put(j, 0, s)
    for i in range(1, M.size):
        for j in range(1, M.size):
            global_min = min(A.at(i-1, j), A.at(i, j-1))
            A.put(i, j, global_min + M.at(i, j))
    return A.at(A.size-1, A.size-1)

def get_neighbors(G, pos):
    assert type(pos) == tuple, "argument %r is not a tuple" % pos
    assert len(pos) == 2, "argument %r is not of length 2"
    assert all([type(n) == int for n in pos]), "argument %r is not composed of integers"
    i,j = pos
    bound = G.size
    neighbors = []
    if i+1 < bound: # can move right
        neighbors.append((i+1,j))
    if i-1 >= 0: # can move left
        neighbors.append((i-1,j))
    if j+1 < bound: # can move down 
        neighbors.append((i,j+1))
    if j-1 >= 0: # can move up
        neighbors.append((i,j-1))
    return neighbors

def dist(G,v):
    i,j = v
    return G.at(i,j)

