from collections import deque
import sys
input = sys.stdin.readline

input()

N, M, K = map(int, input().split())     # 총 지원 비용 : M
graph = [[] for _ in range(N+1)]
for _ in range(K):
    u, v, c, d = map(int, input().split())      # 출발지, 도착지, 비용, 소요시간
    graph[u].append((v, c, d))

start, end = 1, N
q = deque()
q.append((0, start, 0))      # 시간, 정점, 현재까지 비용

distance = [[1e9]*(M+1) for _ in range(N+1)]
distance[start][0] = 0


while q:
    time, now, fee = q.popleft()

    if distance[now][fee] < time:
        continue

    for v, f, t in graph[now]:
        newf = fee + f
        if newf > M:
            continue

        cost = time + t
        if cost < distance[v][newf]:
            for i in range(newf, M+1):
                if cost < distance[v][i]:
                    distance[v][i] = cost
                else:
                    break

            q.append((cost, v, newf))

ans = distance[N][M]
print(ans if ans < 1e9 else "Poor KCM")

