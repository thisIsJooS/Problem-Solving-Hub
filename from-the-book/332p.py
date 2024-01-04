from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def closest_2(x, y, comb):
    min_dist = 1e9
    for c in comb:
        a, b = c
        dist = abs(x-a) + abs(y-b)
        min_dist = min(dist, min_dist)

    return min_dist


chickens = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chickens.append((i, j))


result = 1e9
for comb in combinations(chickens, M):
    res = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                dist = closest_2(i, j, comb)
                res += dist

    result = min(result, res)

print(result)