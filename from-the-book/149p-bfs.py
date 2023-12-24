from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

def get_child(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    ret = []

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not (0<=nx<n and 0<=ny<m):
            continue
        ret.append((nx, ny))

    return ret


res = 0
for x in range(n):
    for y in range(m):
        if board[x][y] == 0:
            queue = deque([(x, y)])
            board[x][y] = 2

            while queue:
                v = queue.popleft()

                for nx, ny in get_child(v[0], v[1]):
                    if board[nx][ny] == 0:
                        queue.append((nx, ny))
                        board[nx][ny] = 2

            res += 1

print(res)







""" inputs
4 5
00110
00011
11111
00000
"""#3

"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""#8

