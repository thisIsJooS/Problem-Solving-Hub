from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    weight = [0] + list(map(int, input().split()))

    indeg = [0] * (n+1)
    dp = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    q = deque()

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indeg[b] += 1

    for i in range(1, n+1):
        if indeg[i] == 0:
            q.append(i)
            dp[i] = weight[i]

    while q:
        now = q.popleft()

        for v in graph[now]:
            indeg[v] -= 1
            dp[v] = max(dp[v], dp[now] + weight[v])

            if indeg[v] == 0:
                q.append(v)

    end = int(input())
    print(dp[end])

