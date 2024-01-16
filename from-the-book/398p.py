import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
planets = []

def get_dist(a, b):
    return min(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))


for _ in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z))



for i in range(n):
    for j in range(i+1, n):
        dist = get_dist(planets[i], planets[j])
        graph[i].append((j, dist))
        graph[j].append((i, dist))


import heapq

visited = set()
q = []
start = 0
heapq.heappush(q, (0, start))
res = 0

while q:
    dist, now = heapq.heappop(q)

    if now in visited:
        continue

    visited.add(now)
    res += dist

    for v, d in graph[now]:
        if v not in visited:
            heapq.heappush(q, (d, v))


print(res)