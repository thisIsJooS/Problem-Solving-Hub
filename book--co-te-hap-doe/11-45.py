# https://school.programmers.co.kr/learn/courses/30/lessons/67259#

import heapq
from collections import defaultdict

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

V = 0
H = 1


def solution(board):
    answer = 0

    n = len(board)
    total_cost = [[[1e9 for _ in range(n)] for _ in range(n)] for _ in range(2)]
    q = []

    # (지금까지 비용, x, y, 이전 방향)
    heapq.heappush(q, (0, 0, 0, 0))
    heapq.heappush(q, (0, 0, 0, 1))

    total_cost[0][0][0] = 0
    total_cost[1][0][0] = 0

    while q:
        cost, x, y, direction = heapq.heappop(q)

        if total_cost[direction][x][y] < cost:
            continue

        if x == n - 1 and y == n - 1:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if board[nx][ny]:
                continue

            new_direction = V if y == ny else H

            if direction != new_direction:
                additional_cost = 600
            else:
                additional_cost = 100

            new_cost = cost + additional_cost
            if total_cost[new_direction][nx][ny] >= new_cost:
                total_cost[new_direction][nx][ny] = new_cost
                heapq.heappush(q, (new_cost, nx, ny, new_direction))

            # print(x, y, '/', nx, ny,'/', direction, new_direction, '/', cost, new_cost)

    return min(total_cost[0][n - 1][n - 1], total_cost[1][n - 1][n - 1])