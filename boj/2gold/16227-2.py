import sys
input = sys.stdin.readline
from heapq import *

INF = 1e9
N, K = map(int, input().split())
start, end = 0, N+1
graph = [[] for _ in range(N+2)]
for _ in range(K):
    u, v, t = map(int, input().split())
    if t <= 100:
        if u == 0 or v == 0 or u == N+1 or v == N+1:
            (u, v) = sorted((u, v))
            graph[u].append((v, t))

        else:
            graph[u].append((v, t))
            graph[v].append((u, t))


dp = [[INF] * (101) for _ in range(N+2)]    # dp[node][지금까지 간 시간 ([0, 100])] = time
dp[start][0] = 0
q = []
heappush(q, (0, 0, 0))  # 시간, 현재 정점, 정비 전 운행한 거리
ans = None

while q:
    time, now, prev_time = heappop(q)

    if now == N+1:
        ans = time
        break

    for v, t in graph[now]:
        new_time = time + t
        new_prev_time = prev_time + t
        if prev_time + t > 100:
            new_time += 5
            new_prev_time = t

        if dp[v][new_prev_time] > new_time:
            dp[v][new_prev_time] = new_time
            heappush(q, (new_time, v, new_prev_time))


print(ans)
