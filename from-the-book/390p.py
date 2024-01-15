import heapq

n, m = map(int, input().split())

mat = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    mat[a].append(b)
    mat[b].append(a)

start = 1
dist = [1e9] * (n+1)
dist[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    d, now = heapq.heappop(q)

    if dist[now] < d:
        continue

    for v in mat[now]:
        cost = dist[now] + 1
        if cost < dist[v]:
            dist[v] = cost
            heapq.heappush(q, (cost, v))



max_val = max(dist[1:])
max_index = dist.index(max_val)
print(max_index, max_val, dist.count(max_val))


"""
6 7
3 6 
4 3
3 2
1 3
1 2
2 4
5 2
"""