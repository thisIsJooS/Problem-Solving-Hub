"""
0 : union
1: 같은 팀 여부 확인
"""
n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    i, a, b = map(int, input().split())

    if i == 0:  #union
        union(a, b)
    else:
        a = find_parent(a)
        b = find_parent(b)

        if a == b:
            print('YES')
        else:
            print('NO')


"""input
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""


