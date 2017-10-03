def read_matrix(path='matrix.txt'):
    m = []
    for line in open(path, 'r').read():
        m.append(line.split())

M = [ [131,673,234,103,18], [201,96,342,956,150], [630,803,746,422,111], [537,699,497,121,956], [805,732,524,37,331]]

class matrix:
    def __init__(self, size):
        self.size = size
        self.this = [[0 for i in range(size)]] * size
    def build_from_vector(self, vector):
        assert self.size**2 == len(vector)
        i, j = 0, 0 
        for item in vector:
            if i == self.size:
                i = 0
                j += 1
            self.put(i, j, item)
            i += 1
    def at(self, x, y):
        return self.this[y][x]
    def put(self, x, y, item):
        self.this[y][x] = item
    def pprint(self):
        for vector in self.this:
            print(vector)

a = matrix(2)
a.build_from_vector([1,2,3,4])
a.pprint()

def get_path(M):
    n = len(M)
    A = [[0 for i in range(n)]] * n
    A[0] = [sum(M[0][:x]) for x in range(1,n+1)]
    temp = [0] * n
    for i in range(n): 
        temp[i] = sum([v[0] for v in M[:i+1]])
    for i in range(len(temp)):
        print(temp[i])
        A[i][0] = temp[i]
    for v in A:
        print(v)
    # for i in range(2, n):
    #     for j in range(2,n):
    #         A[i][j] = min(A[i-1][j], A[i][j-1]) + M[i][j]
    # return A
