import sys
from math import inf
sys.path.append('/Users/oppenheimer/broject_euler')
from utils import matrix
from itertools import product

M = [131,673,234,103,18,201,96,342,956,150,630,803,746,422,111,537,699,497,121,956,805,732,524,37,331]
M = matrix(5, M)

def make_answer(G):
    n = G.size-1
    distances, prev = dijkstras(G, (0,0))
    path_cost = get_path_cost(G, reconstruct_path(prev, (n,n)))
    return path_cost

def read_matrix(path='matrix.txt'):
    ans = []
    for line in open(path, 'r'):
        l = [int(i) for i in line[:-1].split(',')]
        ans += l
    return ans

def make_q(l):
    return sorted(product(range(l), repeat=2), key=lambda t: sum(t))

def make_neighbor_adjacency(G):
    d = dict()
    for node in make_q(G.size):
        d[node] = get_neighbors(G, node)
    return d

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

def length(G, v):
    i,j = v
    return G.at(i,j)

def dijkstras(G, s):
    dist = dict()
    prev = dict()
    Q = make_q(G.size)
    for pos in Q:
        dist[pos] = inf
    dist[(0,0)] = 0
    while Q:
        u = Q.pop(0)
        for v in get_neighbors(G, u):
            alt = dist[u] + length(G, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev

def reconstruct_path(dictionary, source):
    ans = []
    try: 
        while dictionary[source]:
            ans.insert(0, source)
            source = dictionary[source]
    finally:
        return ans

def get_path_cost(G, sequence):
    s = [G.at(0,0)]
    for i,j in sequence: s.append(G.at(i,j))
    return sum(s)

G = read_matrix()
G = matrix(int(len(G)**(1/2)), G)
print(make_answer(G))

