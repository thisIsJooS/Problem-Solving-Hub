# https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(board):
    answer = 0

    n, m = len(board), len(board[0])

    visited = [[False] * m for _ in range(n)]
    start = get_start_point(board)
    target = get_target_point(board)
    visited[start[0]][start[1]] = True

    q = deque()
    q.append((start, 0))

    while q:
        (x, y), cost = q.popleft()

        for i in range(4):
            nx, ny = x, y

            while is_valid(board, nx + dx[i], ny + dy[i]):
                nx, ny = nx + dx[i], ny + dy[i]

            if (nx, ny) == (x, y) or visited[nx][ny]:
                continue

            if (nx, ny) == target:
                return cost + 1

            visited[nx][ny] = True
            q.append(((nx, ny), cost + 1))

    return -1


def get_start_point(board):
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                return i, j


def get_target_point(board):
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'G':
                return i, j


def is_valid(board, x, y):
    n = len(board)
    m = len(board[0])

    if not (0 <= x < n and 0 <= y < m):
        return False

    if board[x][y] == 'D':
        return False

    return True
