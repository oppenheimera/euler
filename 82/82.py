import sys
from math import inf
sys.path.append('/Users/oppenheimer/broject_euler')
from utils import matrix

M = [131,673,234,103,18,201,96,342,956,150,630,803,746,422,111,537,699,497,121,956,805,732,524,37,331]
M = matrix(5, M)
path = [201, 96, 342, 234, 103, 18]

def test():
    assert get_path(M) == 994

def read_matrix(path='matrix.txt'):
    ans = []
    for line in open(path, 'r'):
        l = [int(i) for i in line[:-1].split(',')]
        ans += l
    return ans

def get_path(M):
    A = matrix(M.size)
    for i in range(M.size): # set A_{i,j} = infinity
        for j in range(M.size):
            A.put(i, j, inf)
    for i in range(M.size): # set A_{0,0...n-1} to be M_{i,j}
        A.put(0, i, M.at(0, i))

    for i in range(1, M.size): # do the work
        for j in range(M.size):
            weight = A.at(i-1,j) + M.at(i,j)
            A.put(i,j, weight)
        for k in range(M.size):
            if j == 0:
                alt = A.at(i, k+1) + M.at(i, k)
                if alt < A.at(i,k):
                    A.put(i,k, alt)
            if j == M.size-1:
                alt = A.at(i, k-1) + M.at(i, k) 
                if alt < A.at(i,k):
                    A.put(i,k, alt)
            else:
                alt1 = A.at(i, k-1) + M.at(i, k)
                alt2 = A.at(i, k+1) + M.at(i, k)
                alt = min(alt1, alt2)
                if alt < A.at(i,k):
                    A.put(i,k, alt)
    A.pprint()
    # return A.at(A.size-1, A.size-1)

def get_min(G, i, j):
    if j == 0:
        lowerL = G.at(i-1, j+1) + G.at(i-1, j) + G.at(i, j)
        line = G.at(i-1, j) + G.at(i, j)
        ans = min(lowerL, line)
    if j == G.size - 1:
        upperL = G.at(i-1, j-1) + G.at(i-1, j) + G.at(i,j)
        line =  G.at(i-1, j) + G.at(i, j)
        ans = min(upperL, line)
    else:
        upperL = G.at(i-1, j-1) + G.at(i-1, j) + G.at(i,j)
        line = G.at(i-1, j) + G.at(i, j)
        lowerL = G.at(i-1, j+1) + G.at(i-1, j) + G.at(i, j)
        ans = min(upperL, line, lowerL)
    return ans

def get_col_min(G, col):
    vector = []
    for j in range(G.size):
        v.append(G.at(col, j))
    return min(vector)

# get_path(matrix(int(len(M)**(1/2)), M))
