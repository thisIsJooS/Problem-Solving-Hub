import heapq, sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    q = []
    heapq.heappush(q, (0, 1))
    visited = set()
    res = 0

    while q:
        cost, now = heapq.heappop(q)

        if now in visited:
            continue

        res += cost
        visited.add(now)

        for v in graph[now]:
            if v not in visited:
                heapq.heappush(q, (1, v))

    print(res)