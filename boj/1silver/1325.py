from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


arr = [0 for _ in range(n+1)]
for i in range(1, n+1):
    cnt = 1
    visited = [False] * (n+1)
    visited[i] = True
    q = deque()
    q.append(i)

    while q:
        now = q.popleft()

        for v in graph[now]:
            if visited[v]: continue

            visited[v] = True
            cnt += 1
            q.append(v)

    arr[i] = cnt

max_val = 0
ans = []
for i in range(1, n+1):
    if arr[i] == max_val:
        ans.append(i)
    elif arr[i] > max_val:
        ans = [i]
        max_val = arr[i]

print(*ans)