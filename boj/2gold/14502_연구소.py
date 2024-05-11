from itertools import combinations
import copy
from collections import deque

def solution():
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    safes = []

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                safes.append((i, j))

    answer = 0
    for comb in combinations(safes, 3):
        answer = max(answer, f(copy.deepcopy(maps), comb))

    return answer


def f(maps, comb):
    for c in comb:
        x, y = c
        maps[x][y] = 1

    n = len(maps)
    m = len(maps[0])

    visited = [[False]*m for _ in range(n)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 2:
                continue

            if visited[i][j]:
                continue

            visited[i][j] = True
            q = deque()
            q.append((i, j))

            while q:
                x, y = q.popleft()

                for p in range(4):
                    nx, ny = x+dx[p], y+dy[p]

                    if not (0<=nx<n and 0<=ny<m):
                        continue

                    if maps[nx][ny] == 1:
                        continue

                    if visited[nx][ny]:
                        continue

                    visited[nx][ny] = True
                    maps[nx][ny] = 2
                    q.append((nx, ny))

    ret = 0
    for i in range(n):
        ret += maps[i].count(0)

    return ret


print(solution())
