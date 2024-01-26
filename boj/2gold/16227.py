"""
80% 에서 틀림!
정답은 16227-2.py 에서
"""

import sys
input = sys.stdin.readline

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


dp = [[[INF, 0, None]] * (K+1) for _ in range(N+2)]    # dp[node][거쳐간횟수] = (time, 충전한 횟수, 정비 전 운행한 거리)
dp[start][0] = [0, 0, 0]

for stop in range(K):
    for node in range(N+1):
        time, cnt, prev = dp[node][stop]
        if time == INF:
            continue

        for v, t in graph[node]:
            new_time = time + t

            if dp[v][stop+1][0] > new_time:
                if prev + t > 100:
                    dp[v][stop+1] = [new_time, cnt+1, t]
                else:
                    dp[v][stop+1] = [new_time, cnt, prev+t]

for i in range(len(dp)):
    for j in range(len(dp[0])):
        if dp[i][j][0] == INF:
            dp[i][j][0] = None

# print(*dp, sep='\n')
arr = dp[N+1]
ans = 1e9
for i in range(K+1):
    time, cnt, _ = arr[i]
    if time == None: continue
    ans = min(ans, time + 5*cnt)

print(ans)




"""
1 2
0 1 1
1 2 1

2

2 4
0 1 40
1 2 60
0 2 110
2 3 10


"""