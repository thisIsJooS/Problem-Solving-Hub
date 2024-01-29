import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
res = [0] * (n+1)

for i in range(1, n+1):
    if res[i] == 0:
        cnt += 1
        q = deque()
        q.append(i)
        res[i] = cnt

        while q:
            now = q.popleft()

            for v in graph[now]:
                if res[v] == 0:
                    res[v] = cnt
                    q.append(v)

print(cnt)