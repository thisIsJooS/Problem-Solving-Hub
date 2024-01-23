from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b  = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

res_bfs = []
res_dfs = []

# bfs
q = deque()
q.append(V)
res_bfs.append(V)

while q:
    now = q.popleft()

    for v in graph[now]:
        if v not in res_bfs:
            res_bfs.append(v)
            q.append(v)


def f(now):
    res_dfs.append(now)

    for v in graph[now]:
        if v not in res_dfs:
            f(v)

f(V)

print(*res_dfs)
print(*res_bfs)