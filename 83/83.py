import sys
sys.path.append('/Users/oppenheimer/broject_euler')
from utils import matrix
from itertools import product

M = [131,673,234,103,18,201,96,342,956,150,630,803,746,422,111,537,699,497,121,956,805,732,524,37,331]
M = matrix(5, M)

def read_matrix(path='matrix.txt'):
    ans = []
    for line in open(path, 'r'):
        l = [int(i) for i in line[:-1].split(',')]
        ans += l
    return ans

def make_q(l):
    return sorted(product(range(l), repeat=2), key=lambda t: sum(t))

def get_path(M):
    A = matrix(M.size)
    for i in range(M.size): # set A_{i,j} = infinity
        for j in range(M.size):
            A.put(i, j, sys.maxsize)
    A.put(0,0,M.at(0,0))
    Q = make_q(M.size)
    for vertex in Q:
        vertex = Q.pop(0)
        neighbors = get_neighbors(A, vertex)
        for neighbor in neighbors:
            i,j = neighbor
            alt = M.at(i,j) + dist(M, vertex)
            if alt < A.at(i,j):
                A.put(i,j, alt)
    A.pprint()
    return A.at(A.size-1, A.size-1)

def neighbor_dist(G, pos):
    return [dist(G, v) for v in get_neighbors(G, pos)]

def get_neighbors(G, pos):
    # graph agnostic, just returns coordinates
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

