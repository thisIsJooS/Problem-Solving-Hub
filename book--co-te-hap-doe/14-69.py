# https://school.programmers.co.kr/learn/courses/30/lessons/120861


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def solution(keyinput, board):
    answer = []

    d = {'left': 0, 'right': 1, 'up': 2, 'down': 3}
    x, y = 0, 0
    for k in keyinput:
        nx, ny = x + dx[d[k]], y + dy[d[k]]

        if is_valid(board, nx, ny):
            x, y = nx, ny

    return [x, y]


def is_valid(board, x, y):
    n = board[0] // 2
    m = board[1] // 2

    if not (-n <= x <= n and -m <= y <= m):
        return False

    return True


