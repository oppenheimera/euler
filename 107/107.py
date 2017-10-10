import sys
sys.path.append('/Users/oppenheimer/broject_euler')
from math import nan, isnan
from utils import matrix


def read_input_to_matrix(filename):
    arr = []
    f = open(filename, 'r')
    for line in f:
        for char in line.split(","):
            if char == "-" or char == "-\n":
                arr.append(nan)
            else:
                arr.append(int(char))
    n = int(len(arr)**(1/2))
    return matrix(n, arr)

def make_edge_set(M):
    s = []
    for i in range(M.size):
        for j in range(i, M.size):
            if not isnan(M.at(i,j)):
                temp = (i,j), M.at(i,j)
                s.append(temp)
    s = sorted(s, key=lambda x: x[1])
    return s

def kruskals(G):
    A = [set([n]) for n in range(G.size)]
    S = make_edge_set(G)
    edges = []
    for edge in S:
        u, v = edge[0]
        u_set, v_set = find_set(A, u), find_set(A, v)
        if u_set != v_set:
            A.remove(u_set)
            A.remove(v_set)
            A.append(u_set.union(v_set))
            edges.append(edge)
    return edges

def are_disjoint(A, B):
    for elem in A:
        if elem in B:
            return False
    return True

def find_set(S, elem):
    for i in range(len(S)):
        if elem in S[i]:
            return S[i]

def edge_sum(S):
    return sum([n[1] for n in S])

M = read_input_to_matrix('network.txt')
S = make_edge_set(M)
print(edge_sum(S) - edge_sum(kruskals(M)))
