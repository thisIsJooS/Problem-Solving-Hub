import sys
input = sys.stdin.readline
input()
INF = 1e9

N, M, K = map(int, input().split())     # 정점 수, 총 비용, 간선 수
graph = [[] for _ in range(N+1)]
for _ in range(K):
    u, v, c, d = map(int, input().split())  # 출발, 도착, 비용, 시간
    graph[u].append((v, c, d))


dp = [[INF]*(M+1) for _ in range(N+1)]
dp[1][0] = 0

for cost in range(M+1):
    for now in range(1, N+1):
        time = dp[now][cost]

        if time == INF:
            continue

        for v, c, d in graph[now]:
            new_cost = cost + c
            if new_cost > M:
                continue

            new_time = time + d
            if dp[v][new_cost] > new_time:
                dp[v][new_cost] = new_time


ans = min(dp[N])
print(ans if ans != INF else 'Poor KCM')
