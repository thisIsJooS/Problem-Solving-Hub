"""
3
3
554
391
327
5
37201
28091
12181
98920
36515
7
9051153
4121653
0761685
1178323
9407641
5832483
7484834
"""

import heapq

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for _ in range(T):
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, list(input()))))

    dist = [[1e9]*n for _ in range(n)]
    dist[0][0] = mat[0][0]
    q = []
    start = (0, 0)
    heapq.heappush(q, (mat[0][0], start))  # (dist, (x, y))

    while q:
        d, (x, y) = heapq.heappop(q)

        if d > dist[x][y]:
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<n and 0<=ny<n):
                continue

            cost = mat[nx][ny] + d
            if dist[nx][ny] > cost:
                dist[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))

    print(dist[n-1][n-1])