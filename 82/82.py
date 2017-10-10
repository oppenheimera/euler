import sys
from math import inf
sys.path.append('/Users/oppenheimer/broject_euler')
from utils import matrix

M = [131,673,234,103,18,201,96,342,956,150,630,803,746,422,111,537,699,497,121,956,805,732,524,37,331]
M = matrix(5, M)

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
    for col in range(1,M.size):
        update_col(M, A, col)
        improve_row(M, A, col)
    return get_col_min(A, A.size-1)

def update_col(G, M, col):
    """
    M is the matrix being updated.

    This function sums across columns of the matrix G.
    """
    assert G.size == M.size, "G and M are of differing sizes"
    assert col < G.size, "Argument col (%f) is too big" % col
    if col == 0:
        for i in range(G.size): 
            M.put(0,i, G.at(0,i))
    else:
        for j in range(G.size):
            temp = M.at(col-1, j) + G.at(col, j)
            M.put(col, j, temp)

def improve_row(G, M, col):
    """
    M is the matrix being improved, col is the column upon which the procedure is being performed.
    
    This function moves a sliding window down M.(col, 0...n). 
    """
    for j in range(G.size):
        a = [M.at(col, j)]
        if j == 0:
            a += [M.at(col, j+1) + G.at(col, j)]
        if j == G.size-1:
            a += [M.at(col, j-1) + G.at(col, j)]
        else:
            a += [M.at(col, j+1) + G.at(col, j), M.at(col, j-1) + G.at(col, j)]
        if min(a) < M.at(col, j):
            M.put(col, j, min(a))

def get_col_min(G, col):
    vector = []
    for j in range(G.size):
        vector.append(G.at(col, j))
    return min(vector)

G = read_matrix()
G = matrix(int(len(G)**(1/2)), G)
print(get_path(M))

