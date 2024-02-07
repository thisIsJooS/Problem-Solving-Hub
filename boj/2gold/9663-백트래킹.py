n = int(input())

board = [[False]*n for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

res = 0


def f(row):
    global res
    if row == n:
        res += 1
        return

    for col in range(n):
        if is_safe(row, col):
            board[row][col] = True
            f(row+1)
            board[row][col] = False


def is_safe(r, c):
    for i in range(8):
        nr, nc = r, c
        while True:
            nr, nc = nr+dx[i], nc +dy[i]
            if not (0<=nr<n and 0<=nc<n): break
            if board[nr][nc]:
                return False

    return True

f(0)
print(res)