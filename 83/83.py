M = [131,673,234,103,18,201,96,342,956,150,630,803,746,422,111,537,699,497,121,956,805,732,524,37,331]

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