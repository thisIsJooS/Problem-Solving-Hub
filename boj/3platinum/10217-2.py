import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        N, M, K = map(int, input().split())
        graph = [[] for _ in range(N+1)]  # graph[node] = [(next_node, cost, time), ...]
        for _ in range(K):
            u, v, cost, time = map(int, input().split())
            graph[u].append((v, cost, time))
        answer = solve(N, M, graph)

        if answer < 0:
            print("Poor KCM")
        else:
            print(answer)


def solve(N, M, graph):
    INF = 1e9
    dp = [[INF] * (M+1) for _ in range(N+1)]  # dp[node][cost] = time
    dp[1][0] = 0

    for cost in range(M + 1):
        for node in range(1, N+1):
            if dp[node][cost] == INF:
                continue
            time = dp[node][cost]
            for next_node, next_cost, next_time in graph[node]:
                next_cost += cost
                next_time += time
                if next_cost <= M and next_time < dp[next_node][next_cost]:
                    dp[next_node][next_cost] = next_time

    result = min(dp[N])

    return result if result != INF else -1


main()
