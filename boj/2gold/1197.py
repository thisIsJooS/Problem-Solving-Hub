import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

ans = 0
for e in edges:
    c, a, b = e

    if find_parent(a) != find_parent(b):
        union(a, b)
        ans += c

print(ans)
