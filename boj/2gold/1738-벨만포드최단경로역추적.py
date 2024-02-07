n, m = map(int, input().split())
edges = []
INF = 1e11
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

distance = [-INF] * (n+1)
start, end = 1, n
distance[start] = 0
cycle = False
parent = [0 for _ in range(n+1)]

def bf():
    for i in range(n):
        for e in edges:
            a, b, c = e

            cost = distance[a] + c
            if distance[a] != -INF and distance[b] < cost:
                distance[b] = cost
                parent[b] = a

                if i == n-1:
                    distance[b] = INF   # 사이클이 존재한다면, INF 로 표시


bf()
if distance[n] == INF:
    print(-1)
    exit()

path = []
cur = n
while cur:
    path.append(cur)
    cur = parent[cur]

print(*path[::-1])