# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    answer = 1

    n, m = len(maps), len(maps[0])

    maps = [[0] * (m + 2)] + [[0] + m + [0] for m in maps] + [[0] * (m + 2)]

    start, target = (1, 1), (n, m)

    q = deque([(start[0], start[1], 1)])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if maps[nx][ny] in [0, 2]:
                continue

            if nx == n and ny == m:
                return cnt + 1

            q.append((nx, ny, cnt + 1))
            maps[nx][ny] = 2

    return -1