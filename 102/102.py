sample_in = '-340,495,-153,-910,835,-947'
sample_in2 = '-175,41,-421,-714,574,-645'
count = 0

def read_triangle(line):
    points = line.split(',')
    points = [int(point) for point in points]
    A,B,C = tuple(points[:2]), tuple(points[2:4]), tuple(points[4:6])
    return tuple(sorted((A,B,C), key=lambda x: x[1], reverse=True))

def get_m(point_a, point_b):
    a = max((point_a, point_b), key=lambda x: x[1])
    b = min((point_a, point_b), key=lambda x: x[1])
    if a[1] - b[1] == 0:
        return 0
    return (a[1] - b[1]) / (a[0] - b[0])

def origin_in_bounded_area(point_tup):
    A,B,C = point_tup
    m_ab = get_m(A,B)
    m_ac = get_m(A,C)
    def f(tup, m): 
        if m == 0:
            return False
        return (m * tup[0] - tup[1]) / m
    ab = f(A, m_ab)
    ac = f(A, m_ac)
    if max(ab, ac) >= 0 and 0 >= min(ab, ac) and all([ab, ac]):
        return True
    else:
        return False

for line in open('triangles.txt', 'r'):
    try:
        if origin_in_bounded_area(read_triangle(line)):
            count += 1
    except:
        print(line)
        read_triangle(line)

print(count)
