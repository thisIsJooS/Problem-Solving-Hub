from heapq import *

n = int(input())

edges = []
pos = []
graph = [[1e9]*n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for i in range(n):
    a, b = map(float, input().split())
    pos.append((a, b))

for i in range(n-1):
    for j in range(i+1, n):
        x1, y1 = pos[i]
        x2, y2 = pos[j]

        d = pow(((x1-x2)**2 + (y1-y2)**2), 0.5)
        graph[i][j] = d
        graph[j][i] = d


start = 0
q = []
heappush(q, (0, start))
res = 0
visited = set()

while q:
    dist, now = heappop(q)

    if now in visited:
        continue

    visited.add(now)

    res += dist

    for v in range(n):
        if v not in visited:
            heappush(q, (graph[now][v], v))


print(res)




