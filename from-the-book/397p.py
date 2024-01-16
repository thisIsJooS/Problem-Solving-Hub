import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


while True:
    m, n = map(int, input().split())
    if m == n == 0 : exit(0)

    agg = 0
    edges = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
        agg += c

    edges.sort()
    res = 0
    parent = [i for i in range(m)]
    for e in edges:
        c, a, b = e

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            res += c

    print(agg - res)