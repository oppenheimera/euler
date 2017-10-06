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
    for i in range(M.size):
        for j in range(M.size):
            A.put(i, j, sys.maxsize)
    for i in range(M.size): # set up A_{0,i}
        A.put(0, i, M.at(0, i))
    s = 0
    A.pprint()
    for i in range(1, M.size): # do the work
        for j in range(M.size):
            if i == 0:
                global_min = min(A.at()) 
            if i == m.size - 1:
                global_min = 
            else:
                global_min = min(A.at(i, j-1), A.at(i, j+1))
            A.put(i, j, global_min + M.at(i, j) + A.at(i-1, j)) 
    A.pprint()
    return A.at(A.size-1, A.size-1)

get_path(matrix(int(len(M)**(1/2)), M))