n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

from collections import deque
visited = [[False * m] * n]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if not (0<=nx<n and 0<=ny<m):
            continue

        if board[nx][ny] == 0:
            continue

        if board[nx][ny] == 1:      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            board[nx][ny] = board[x][y] + 1
            queue.append((nx, ny))



print(board[n-1][m-1])

"""
5 6
101010
111111
000001
111111
111111
"""