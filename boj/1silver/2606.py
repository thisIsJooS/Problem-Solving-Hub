n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
q = deque()
q.append(1)
visited = set()
visited.add(1)

while q:
    now = q.popleft()

    for v in graph[now]:
        if v not in visited:
            q.append(v)
            visited.add(v)

print(len(visited)-1)