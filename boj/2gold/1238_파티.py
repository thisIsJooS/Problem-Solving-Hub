from collections import deque, defaultdict

def solution():
    n, m, x = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    distance = [[1e9] * (n+1) for _ in range(n+1)]

    answer = 0

    for start in range(1, n+1):
        distance[start][start] = 0

        q = deque()
        q.append((start, 0))

        while q:
            now, dist = q.popleft()

            if distance[start][now] < dist:
                continue

            for v, c in graph[now]:
                cost = dist + c
                if distance[start][v] > cost:
                    distance[start][v] = cost
                    q.append((v, cost))


    for i in range(1, n+1):
        dist = distance[i][x] + distance[x][i]
        answer = max(answer, dist)

    print(answer)


solution()

