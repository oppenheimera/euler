import sys
sys.path.append('/Users/oppenheimer/broject_euler')
from utils import matrix

M = [131,673,234,103,18,201,96,342,956,150,630,803,746,422,111,537,699,497,121,956,805,732,524,37,331]

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
            A.put(i, j, sys.maxsize)
    for i in range(M.size): # set A_{0,0...n-1} to be M_{i,j}
        A.put(0, i, M.at(0, i))

    for i in range(1, M.size): # do the work
        for j in range(M.size):
            if j == 0:
                global_min = M.at(i, j) + min(A.at(i-1, j), A.at(i, j+1)) 
            if j == M.size - 1:
                global_min = M.at(i, j) + min(A.at(i-1, j), A.at(i, j - 1))
            else:
                global_min = M.at(i, j) + min(A.at(i, j-1), A.at(i, j+1), A.at(i-1, j))
            A.put(i, j, global_min) 
    A.pprint()
    return A.at(A.size-1, A.size-1)

get_path(matrix(int(len(M)**(1/2)), M))