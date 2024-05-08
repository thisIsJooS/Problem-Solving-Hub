# https://school.programmers.co.kr/learn/courses/30/lessons/150365?language=python3

import sys

sys.setrecursionlimit(10 ** 4)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
direction = ['d', 'l', 'r', 'u']
answer = ''


def solution(n, m, x, y, r, c, k):
    min_move = abs(r - x) + abs(c - y)

    if min_move > k or (k - min_move) % 2:
        return 'impossible'

    dfs(x, y, '', 0, n, m, r, c, k)

    return answer


def dfs(x, y, string, move, n, m, r, c, k):
    global answer

    if k < move + abs(x - r) + abs(y - c):
        return

    if move == k and (x, y) == (r, c):
        answer = string
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if not (0 < nx <= n and 0 < ny <= m):
            continue

        if answer:
            continue

        dfs(nx, ny, string[:] + direction[i], move + 1, n, m, r, c, k)

