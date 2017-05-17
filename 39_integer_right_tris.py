def find_bc(a, P):
    for b in reversed(range(1,P//2)):
        c = P - (a + b)
        if a**2 + b**2 == c**2:
            return a,b,c

def find_solutions(P):
    ans = [P]
    for n in range(1, P//3):
        tri = find_bc(n,P)
        if tri:
            ans.append(tri)
    return ans

ans = []
for n in range(2,1001,2):
    tri = find_solutions(n)
    if len(tri) > 1:
        ans.append(tri)

print(max(ans, key=len))
