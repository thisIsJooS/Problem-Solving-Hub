from heapq import heappush, heappop

def solution(land, height):
    answer = 0
    n = len(land)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * n for _ in range(n)]

    q = []
    heappush(q, (0, 0, 0))

    while q:
        cost, x, y = heappop(q)

        if visited[x][y]:
            continue

        visited[x][y] = True
        answer += cost

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if not (0<=nx<n and 0<=ny<n):
                continue

            tmp_cost = abs(land[x][y] - land[nx][ny])
            if tmp_cost > height:
                new_cost = tmp_cost
            else:
                new_cost = 0

            heappush(q, (new_cost, nx, ny))


    return answer