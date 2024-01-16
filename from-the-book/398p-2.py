import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
planets = []

def get_dist(a, b):
    return min(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z))

edges = []

for i in range(n):
    for j in range(i+1, n):
        dist = get_dist(planets[i], planets[j])
        edges.append((dist, i, j))


start = 0
edges.sort()
res = 0
parent = [i for i in range(n)]


for e in edges:
    d, a, b = e

    if find(a) != find(b):
        union(a, b)
        res += d


print(res)