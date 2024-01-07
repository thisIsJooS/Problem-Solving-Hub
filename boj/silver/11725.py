import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n+1)]
start = 1
parent[start] = 0

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
q = deque()
q.append(start)
visited = set()
visited.add(start)

while q:
    now = q.popleft()

    for v in graph[now]:
        if v not in visited:
            parent[v] = now
            q.append(v)
            visited.add(v)

for p in parent[2:]:
    print(p)

